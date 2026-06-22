import json
import random
import re
import sys

from filter import FILTER_CONFIG, compile_filter_config, evaluate_block;

def sample(document: dict, parameters: dict) -> bool:
    """
    Inputs:
        document - json document
        parameters - dictionary, including .tokens. count    Returns True for documents to keep and False for documents to discard
    Returns True for documents to keep and False for documents to discard
    """

    token_count = parameters["tokens"];

    # REGISTER VARIABLES
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

    COMPILED_FILTERS = compile_filter_config(FILTER_CONFIG)

    # if document do not pass the filter we return 0
    if not evaluate_block(document, COMPILED_FILTERS["and"]):
        return False

    if COMPILED_FILTERS["or"]:
        passed_or = any(
            evaluate_block(document, block)
            for block in COMPILED_FILTERS["or"]
        )

        if not passed_or:
            return False

    if len(document.get("text", "")) < 200:
        return False

    # special case for small languages:
    # we can identify a noisy document by it having "noise" field,
    # according to Stephan: https://github.com/OpenEuroLLM/Taskboard/issues/219#issuecomment-4732960717
    is_noisy = "noise" in document
    if token_count < 15e9 and not is_noisy:
        return True

    # handle registers
    probs = document.get("web-register", None)
    if probs:
        r = assign_labels(probs, 0.4)
        if is_hybrid(r) and r != {"HI", "IN"}:
            return False
    
    return True

def main():
    for line in sys.stdin:
        _ = json.loads(line.strip());
        _["score"] = sample(_, {"tokens": random.uniform(1e8, 1e12)});
        print(json.dumps(_));
        
if __name__ == "__main__":
    main();
