#!/usr/bin/env python

# -*- coding: utf-8; -*-

from collections import Counter;
import argparse;
import glob;
import io;
import json;
import math;
import os;
import re;
import sys;
import time;

def main():

  start = time.time();

  parser = argparse.ArgumentParser(description = "Maintenance of OpenEuroLLM Training Data Collection");
  parser.add_argument("--pattern", type = str, default = None);
  parser.add_argument("--counts", type = str, default = "source.json");
  parser.add_argument("--format", type = str, default = "plain");
  parser.add_argument("--sum", action = "store_true", default = False);
  parser.add_argument("--budget", action = "store_true", default = False);
  parser.add_argument("--finepdfs", action = "store_true", default = False);
  parser.add_argument("--hplt", action = "store_true", default = False);
  parser.add_argument("--quiet", action = "store_true", default = False);
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

  mix = dict();
  if arguments.budget or arguments.finepdfs or arguments.hplt:
    pattern = re.compile(r"(0\.[0-9]+)[ \t](.+)$")
    
    with open(arguments.inputs[0], encoding = "utf-8") as stream:
      for i, line in enumerate(stream):
        line = line.strip();
        _ = pattern.match(line)
        if _ is None:
          if not arguments.quiet:
            print("plan.py(): ignoring line #{}: {}."
                  "".format(i, line),
                  file = sys.stderr, flush = True);
          continue;
        ratio, path = _.groups();
        mix[path] = float(ratio);

  if arguments.budget or arguments.hplt:
    pattern = None;
    if arguments.pattern is not None: pattern = re.compile(arguments.pattern);
    elif arguments.hplt: pattern = re.compile(r"hplt-");
    for path, ratio in mix.items():
      if pattern is not None and pattern.search(path) is None: continue
      _ = os.path.join(path.replace("/megatron-lm", "/counts"), arguments.counts)
      if not os.path.isfile(_):
        if not arguments.quiet:
          print("plan.py(): no counts for {} (#{})."
                "".format(path, i),
                file = sys.stderr, flush = True);
        continue;
      with open(_, encoding = "utf-8") as _:
        counts = json.load(_);
        budget = math.ceil(1e13 * ratio / 1e6);
        pool = math.floor(counts["tokens"] / 1e6);
        percent = budget / pool * 100;
        if arguments.hplt:
          _ = os.path.join(path.replace("/megatron-lm", "/counts"), "wds+register.json")
          if not os.path.isfile(_):
            if not arguments.quiet:
              print("plan.py(): no wds+register counts for {} (#{})."
                    "".format(path, i),
                    file = sys.stderr, flush = True);
            continue;
          with open(_, encoding = "utf-8") as _:
            new = json.load(_);
            part = re.sub(r"[^/]+/megatron-lm/", "", path);
            print("{}: {:,}m / {:,} source tokens = |{:,.1f}|; "
                  "{:,}m / {:,} wds+register tokens = |{:,.1f}| "
                  "({:,.1f}% / {:,.1f}%)."
                  "".format(part, counts["tokens"] // 1e6, counts["documents"],
                            counts["tokens"] / counts["documents"],
                            new["tokens"] // 1e6, new["documents"],
                            new["tokens"] / new["documents"],
                            new["tokens"] / counts["tokens"] * 100,
                            new["documents"] / counts["documents"] * 100));
        elif arguments.format == "plain":
           print("{}: {:,}m tokens of {:,}m ({:,.1f}%)."
                 "".format(path, budget, pool, percent));
        elif arguments.format == "yaml":
          print("  {}:".format(re.sub(r".+/megatron-lm/", "", path)));
          percent = math.ceil(percent);
          if percent >= 100:
            print("    sample: full");
          else:
            print("    budget: {}%".format(percent));
    sys.exit(0);

  if arguments.finepdfs:
    for path, ratio in mix.items():
      if path.startswith("finepdfs-1.0.0"):
        edu = path.replace("finepdfs-1.0.0", "finepdfs-edu-1.0.0");
        if edu not in mix:
          print("{:,.6f} {}".format(ratio, path));
          continue;
        sum = ratio + mix[edu];
        _ = os.path.join(edu.replace("/megatron-lm", "/counts"), arguments.counts)
        with open(_, encoding = "utf-8") as _:
          r = min(sum, json.load(_)["tokens"] / 1e13);
          print("{:,.6f} {}".format(r, edu));
          if sum > r: print("{:,.6f} {}".format( sum - r, path));
    sys.exit(0);
    

if __name__ == "__main__":
  main();
