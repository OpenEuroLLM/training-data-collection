import re
import math
import json
import random
import numpy as np
from scipy.optimize import fsolve

# Variables for scoring function and
L_wds = 0.5 # weight for WDS
L_bsc = 1.0 # weight for bsc-edu
L_reg = 1.0 # weight for register 
k_bsc = 2.2 # steepnees of bsc-edu sigmoid

# This is the most important parameter!
midp_bsc = 2.5 # midpoint of bsc-edu sigmoid ! 
# Increase it for harsher filtering
# Or decrease to accept more low quality data

k_main = 3.4 # steepnees of u/d-sampling

# Document must have those propella categories
FILTER_CONFIG = {
    "and": {
        "propella": {
            "content_integrity": ["complete", "mostly_complete", "fragment"],
            "content_quality": ["excellent", "good", "adequate", "poor"],
            "content_safety": ["safe", "mild_concerns", "nsfw"],
            "content_ratio": ["complete_content","mostly_content","mixed_content","mostly_navigation"],
            "information_density": ["dense","adequate","moderate","thin"]
        }
    }
}


def sample(document: dict, paramters: dict, sampling="linear"):
    """
    Inputs:
        document - json document
        parameters - dictionary, including .tokens. count
        sampling - sampling strategy, by default it's 'linear', but we can also use 'flat' and 'ease_in_out'
    Returns sampling ratio S in range 0 - 4
    """

    token_count = parameters["tokens"];
    
    def propella_hq(record):
        # Assign score based on propella quality metrics
        score = 0.0
        prop = record.get('propella-4b',{})
        cq = prop.get('content_quality',{})
        ed = prop.get('educational_value',{})

        # we boost slightly documents with high edu categories
        # sampling ratio mainly depends on bsc-edu but propella edu was 2nd strongest filter
        if ed == 'high':
            score += 0.1
        elif ed == 'moderate':
            score += 0.05
        elif ed == 'minimal':
            score -= 0.1
        
        # well formated documents are slightly boosted as well
        if cq == 'excellent':
            score += 0.05
        elif cq == 'good':
            score += 0.01
        elif cq == 'poor':
            score -= 0.2
        
        # we would like to retain evergreen documents
        if prop.get('time_sensitivity',{}) == 'evergreen':
            score += 0.03
        
        # we decrease the score for the weakest acceptable categories
        # of content ratio, density and integrity
        if prop.get('content_ratio',{}) == 'mostly_navigation':
            score -= 0.2
        if prop.get('information_density',{}) == 'thin':
            score -= 0.2
        if prop.get('content_integrity',{}) == 'fragment':
            score -= 0.2
        return score


    def interpolate_ratio(tokens_b, anchor_tokens_b, anchor_values):
        """
        Linear interpolation to estimate min and max sampling ratio depending on token count
        """
        x = np.log10(tokens_b)
        xp = np.log10(anchor_tokens_b)
        fp = np.array(anchor_values, dtype=float)
        return float(np.interp(x, xp, fp))


    def get_size_ratios(tokens):
        """
        Returns (min_ratio, max_ratio) based on total token count.
        """
        tokens_b = tokens / 1e9 # for simplification I wrote anchor points in BT
        min_ratio = interpolate_ratio(tokens_b, TOKEN_ANCHORS_B, MIN_ANCHORS)
        max_ratio = interpolate_ratio(tokens_b, TOKEN_ANCHORS_B, MAX_ANCHORS)
        min_ratio = min(min_ratio, max_ratio) # make sure that min !> max
        return min_ratio, max_ratio


    def get_sigmoid_center(k):
        # of stepeness is adjusted sigmoid mid-point need to change as well
        objective = lambda x0: 4 * (np.tanh(k * (0.25 - x0)) + np.tanh(k * x0)) / (
            np.tanh(k * (1 - x0)) + np.tanh(k * x0)
        ) - 1
        initial_guess = 0.25 if k > 10 else 0.35
        return fsolve(objective, initial_guess)[0]

    x0_main = get_sigmoid_center(k_main)

    def tanh_ease_in_out(k, x, x0, maxpoint, shift):
        """
        maxpoint - maximal value of sigmoid
        shift    = lower bound of the range
        """
        return maxpoint * (np.tanh(k * (x - x0)) + np.tanh(k * x0)) / (np.tanh(k * (1 - x0)) + np.tanh(k * x0)) + shift

    # REGISTER VARIABLES
    REGISTERS = ["dtp", "HI", "HI-IN", "ID", "IN", "IP", "MT", "NA", "ne", "OP", "SP", "LY", "no-label"]
    LABEL_HIERARCHY = {
        "MT": [], "LY": [], "SP": ["it"], "ID": [],
        "NA": ["ne", "sr", "nb"], "HI": ["re"],
        "IN": ["en", "ra", "dtp", "fi", "lt"],
        "OP": ["rv", "ob", "rs", "av"], "IP": ["ds", "ed"],
    }
    LABEL_PARENT = {c: p for p, cs in LABEL_HIERARCHY.items() for c in cs}

    # Same logic as previously in HPLT3.0
    def assign_labels(probabilities, threshold=0.4):
        labels = set()
        for label, prob in probabilities.items():
            if prob >= threshold:
                labels.add(label)
                if label in LABEL_PARENT:
                    labels.add(LABEL_PARENT[label])
        return labels

    def is_hybrid(labels):
        if len(labels) > 2:
            return True
        if len(labels) == 2:
            l1, l2 = list(labels)
            return not (
                (l1 in LABEL_PARENT and LABEL_PARENT[l1] == l2) or 
                (l2 in LABEL_PARENT and LABEL_PARENT[l2] == l1)
            )
        return False

    def parse_numeric_rule(rule_str):
        rule_str = str(rule_str).strip()
        match = re.match(r"^([>=<!]+)?\s*([\d.-]+)$", rule_str)
        if not match:
            try: return ("==", float(rule_str))
            except ValueError: return None
        op, num_str = match.groups()
        return (op or "==", float(num_str))

    # Compile filter block
    def compile_single_block(block_dict):
        """Compiles a dictionary block into execution patterns."""
        compiled = {"propella": {}, "root": {}}
        if not block_dict: return compiled
        
        if "downsample" in block_dict:
            compiled["downsample"] = float(block_dict["downsample"])
            
        if "propella" in block_dict:
            for feat, rules in block_dict["propella"].items():
                if isinstance(rules, str): rules = [rules]
                # Numeric evaluation checks
                # score ar can be removed, it was correlation scoring func.
                if feat == "score_AR" or feat.endswith(("_score", "_value")) or any(isinstance(r, (int, float)) or any(o in str(r) for o in ['>', '<', '=']) for r in rules):
                    parsed = [parse_numeric_rule(r) for r in rules if parse_numeric_rule(r)]
                    compiled["propella"][feat] = ("numeric", parsed)
                else:
                    compiled["propella"][feat] = ("categorical", set(str(r) for r in rules))
                    
        for signal, rules in block_dict.items():
            if signal in ["downsample", "propella"]: continue
            if isinstance(rules, (int, float)):
                compiled["root"][signal] = [(">=", float(rules))]
            else:
                if isinstance(rules, str): rules = [rules]
                compiled["root"][signal] = [parse_numeric_rule(r) for r in rules if parse_numeric_rule(r)]
                
        return compiled


    def compile_filter_config(config_dict):
        """Handles parsing AND/OR logic for filters"""
        if "and" not in config_dict and "or" not in config_dict:
            return {
                "and": compile_single_block(config_dict),
                "or": []
            }
        
        return {
            "and": compile_single_block(config_dict.get("and", {})),
            "or": [compile_single_block(b) for b in config_dict.get("or", [])]
        }

    # if we want to use e.g. bsc >= 2.0 filter
    def match_numeric(val, parsed_rules):
        try: val = float(val)
        except (ValueError, TypeError): return False
        for op, num in parsed_rules:
            if op == ">=" and not (val >= num): return False
            elif op == "<=" and not (val <= num): return False
            elif op == ">" and not (val > num): return False
            elif op == "<" and not (val < num): return False
            elif op == "==" and not (val == num): return False
            elif op == "!=" and not (val != num): return False
        return True

    def evaluate_block(record, compiled_block):
        """Evaluates whether a single compiled criterion dictionary evaluates to True."""
        # 1. Downsample
        if "downsample" in compiled_block:
            if random.random() >= compiled_block["downsample"]: return False
                
        # 2. Propella features
        prop = record.get("propella-4b", {})
        if compiled_block["propella"] and prop:
            for feat, (filter_type, rules) in compiled_block["propella"].items():
                val = prop.get(feat)
                if val is None: return False
                
                if filter_type == "numeric":
                    if not match_numeric(val, rules): return False
                else:
                    if isinstance(val, list):
                        if not any(str(v) in rules for v in val): return False
                    else:
                        if str(val) not in rules: return False
                            
        # 3. Standard root quality tracks
        if compiled_block["root"]:
            for signal, rules in compiled_block["root"].items():
                val = record.get(signal)
                if val is None or not match_numeric(val, rules): return False
                    
        return True

    COMPILED_FILTERS = compile_filter_config(FILTER_CONFIG)
    
    # Token count at which we set anchor
    TOKEN_ANCHORS_B = np.array([15, 25, 50, 100, 250, 500], dtype=float)
    # Max sampling value
    MAX_ANCHORS = np.array([4.0, 4.0, 4.0, 4.0, 2.0, 1.0], dtype=float)
    # Min sampling value
    MIN_ANCHORS = np.array([1.0, 1.0, 0.5, 0.005, 0.005, 0.001], dtype=float)

    # if document do not pass the filter we return 0
    if not evaluate_block(document, COMPILED_FILTERS["and"]):
        return 0.0

    if COMPILED_FILTERS["or"]:
        passed_or = any(
            evaluate_block(document, block)
            for block in COMPILED_FILTERS["or"]
        )

        if not passed_or:
            return 0.0

    if len(document.get("text", "")) < 200:
        return 0.0

    min_ratio, max_ratio = get_size_ratios(token_count)

    WDS = document.get("doc_scores", [0])[0] * 10

    # we can identify a noisy document by it having "noise" field,
    # according to Stephan: https://github.com/OpenEuroLLM/Taskboard/issues/219#issuecomment-4732960717
    is_noisy = "noise" in document

    # special case for small languages:
    if token_count < 15e9 and not is_noisy:
        return 1.0

    BSC = document.get("bsc-edu", 0)

    probs = document.get("web-register", None)
    propella_hq_score = propella_hq(document)

    # handle registers
    if probs is None:
        register = "no-label"
    else:
        r = assign_labels(probs, 0.4)
        if len(r) == 0:
            register = "no-label"
        elif is_hybrid(r):
            if r == {"HI", "IN"}:
                register = "HI-IN"
            else:
                return 0.0
        else:
            selected = [j for j in r if j in REGISTERS]
            register = "-".join(sorted(selected))

            if register in ["NA-ne", "ne-NA"]:
                register = "ne"

            if register in ["IN-dtp", "dtp-IN"]:
                register = "dtp"

    reg_up = 0
    if register in ["HI", "HI-IN", "OP", "dtp"]:
        reg_up = 0.1

    # calculate score function
    # In current setting S will go to 0 if WDS is 3
    # so to use scoring function for 'noisy' we would have to clip minimal score to -1 (value for WDS = 5)
    # instead of:      (L_wds * min(0, (WDS - 7) / 2))
    # I'll have:    max(L_wds * min(0, (WDS - 7) / 2),-1)
    score_x = min(
        0.25
        + max(L_wds * min(0, (WDS - 7) / 2),-1)
        + (L_bsc * ((math.tanh(k_bsc * (BSC - midp_bsc)) + 1) / 2))
        + (L_reg * reg_up)
        + propella_hq_score,
        1
    )

    if sampling == "flat":
        S = 1.0

    elif sampling == "linear":
        S = min_ratio + (max_ratio - min_ratio) * score_x

    elif sampling == "ease_in_out":
        S = tanh_ease_in_out(
            k_main,
            score_x,
            x0_main,
            maxpoint=(max_ratio - min_ratio),
            shift=min_ratio
        )

    else:
        raise ValueError(
            f"Unknown sampling mode: {sampling}"
        )
    
    # I use clip to make sure that sampling ratio is not out of bounds
    return float(np.clip(S,min_ratio,max_ratio))
