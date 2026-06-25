import json
import random
import re
import sys

# from filter import FILTER_CONFIG, compile_filter_config, evaluate_block;

#
# do not edit; included from “filter.py”
#

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

#
# end include from “filter.py”
#


def sample(document: dict, parameters: dict = None) -> bool:
    """
    Inputs:
        document - json document
    Returns 1.0 for documents to keep and 0.0 for documents to discard
    """

    COMPILED_FILTERS = compile_filter_config(FILTER_CONFIG)

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

    # we can identify a noisy document by it having "noise" field,
    # according to Stephan: https://github.com/OpenEuroLLM/Taskboard/issues/219#issuecomment-4732960717
    is_noisy = "noise" in document

    # If lang subscore is smallish, and the document is noisy, we reject it
    if is_noisy and "doc_scores" in document and document["doc_scores"][1] < 0.75:
        return 0.0

    return 1.0

def main():
    for line in sys.stdin:
        _ = json.loads(line.strip());
        _["score"] = sample(_);
        print(json.dumps(_));
        
if __name__ == "__main__":
    main();
