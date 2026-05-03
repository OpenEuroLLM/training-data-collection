#!/usr/bin/env python

# -*- coding: utf-8; -*-

from collections import Counter;
import argparse;
import glob;
import io;
import json;
import math;
import os;
import sys;
import time;

def main():

  start = time.time();

  parser = argparse.ArgumentParser(description = "Maintenance of OpenEuroLLM Training Data Collection");
  parser.add_argument("--sum", action = "store_true", default = False);
  parser.add_argument("inputs", nargs = "*");
  arguments = parser.parse_args();

  if arguments.sum:
    result = {"files": 0, "bytes": 0,
              "documents": 0, "segments": 0, "tokens": 0, "characters": 0,
              "time": 0, "errors": 0};
    required = Counter(); optional = set();
    for file in arguments.inputs:
      with open(file) as _:
        counts = json.load(_);
        for _ in ("files", "bytes", "documents", "segments",
                  "tokens", "characters", "time", "errors"):
          result[_] += counts[_];
        if "keys" in counts:
          required.update(counts["keys"]["required"]);
          optional.update(counts["keys"]["optional"]);
          
    n = len(arguments.inputs);
    for key, i in required.items():
      if i < n: optional.add(key);
    result["keys"] = {"required": [_ for _ in required.keys() if not _ in optional],
                      "optional": list(optional)};
    json.dump(result, sys.stdout, indent = 2);
    
  sys.exit(0);

if __name__ == "__main__":
  main();
