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
import yaml;

def summarize_counts(path, argument):
  result = dict();
  for suffix in ["sample", "openeurollm", "source", "release"] if argument is None else [argument]:
    path = path.replace("/megatron-lm", "/counts");
    _ = os.path.join(path, suffix + ".json");
    if os.path.isfile(_):
      with open(_, encoding = "utf-8") as _:
        result[suffix] = json.load(_);
  return result;
  
def main():

  start = time.time();

  parser = argparse.ArgumentParser(description = "Maintenance of OpenEuroLLM Training Data Collection");
  parser.add_argument("--horizon", type = int, default = 15e12);
  parser.add_argument("--pattern", type = str, default = None);
  parser.add_argument("--counts", type = str, default = None);
  parser.add_argument("--format", type = str, default = "plain");
  parser.add_argument("--test", action = "store_true", default = False);
  parser.add_argument("--sum", action = "store_true", default = False);
  parser.add_argument("--budget", action = "store_true", default = False);
  parser.add_argument("--sample", action = "store_true", default = False);
  parser.add_argument("--finepdfs", action = "store_true", default = False);
  parser.add_argument("--quiet", action = "store_true", default = False);
  parser.add_argument("inputs", nargs = "*");
  arguments = parser.parse_args();

  if arguments.counts is not None and arguments.counts.endswith(".json"):
    arguments.counts = arguments.counts[:-len(".json")];

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
  if arguments.test or arguments.budget or arguments.finepdfs or arguments.sample:
    pattern = re.compile(r"(0\.[0-9]+)[ \t](.+)$")
    filter = None;
    if arguments.pattern is not None:
      filter = re.compile(arguments.pattern);
    if arguments.sample:
      arguments.budget = True;
      arguments.format = "sample";
    
    with open(arguments.inputs[0], encoding = "utf-8") as stream:
      for i, line in enumerate(stream):
        line = line.strip();
        if line.startswith("#"): continue;
        _ = pattern.match(line)
        if _ is None:
          if not arguments.quiet:
            print("plan.py(): ignoring line #{}: {}."
                  "".format(i, line),
                  file = sys.stderr, flush = True);
          continue;

        ratio, path = _.groups();
        ratio = float(ratio);
        if ratio == 0:
          if not arguments.quiet:
            print("plan.py(): ignoring line #{}: {}."
                  "".format(i, line),
                  file = sys.stderr, flush = True);
          continue;

        dataset = re.sub(r"/megatron-lm.*", "", path);
        part = re.sub(r".+/megatron-lm/?", "", path);
        counts = summarize_counts(path, arguments.counts);
        active = True if filter is None or filter.search(path) else False;
        mix[path] = {"dataset": dataset, "part": part,
                     "ratio": ratio, "active": active,
                     "counts": counts};
      
  if arguments.test:
    datasets = set();
    for path, data in mix.items():
      if data["active"]: datasets.add(path.split("/")[0]);
    if not arguments.quiet:
      print("plan.py(): {} part(s) in {} dataset(s)."
            "".format(len([_ for _ in mix.values() if _["active"]]),
                      len(datasets)), file = sys.stderr);
    for dataset in datasets:
      metadata = os.path.join(dataset, "metadata.yaml");
      if not os.path.isfile(metadata):
        print("plan.py(): no metadata for {}."
              "".format(dataset), file = sys.stderr);
        continue;
      with open(metadata, encoding = "utf-8") as _:
        metadata = yaml.safe_load(_);
      if "release" not in metadata:
        print("plan.py(): no .release. block in metadata for {}."
              "".format(dataset), file = sys.stderr);
        continue;
      flat = False;
      flats = set();
      for part, data in metadata["release"].items():
        if part in {"default"}:
          if "pack" in data and data["pack"] == "flat": flat = True;
          continue;
        if flat and (data is None or "pack" not in data or data["pack"] == "flat"):
          release = os.path.join(dataset, "release");
          counts = os.path.join(dataset, "counts", "release.json");
          tokens = os.path.join(dataset, "megatron-lm");
          checksums = os.path.join(dataset, "md5", "megatron-lm.md5");
        else:
          release = os.path.join(dataset, "release", part);
          counts = os.path.join(dataset, "counts", part, "release.json");
          tokens = os.path.join(dataset, "megatron-lm", part);
          checksums = os.path.join(dataset, "md5", part, "megatron-lm.md5");
        if not os.path.isdir(release):
          print("plan.py(): no .release. directory for {}."
                "".format(dataset + "/" + part), file = sys.stderr);
        else:
          if not os.path.isfile(counts):
            print("plan.py(): no .release. counts for {}."
                  "".format(dataset + "/" + part), file = sys.stderr);
          elif os.path.getmtime(release) > os.path.getmtime(counts):
            print("plan.py(): out-of-date .release. counts for {}."
                  "".format(dataset + "/" + part), file = sys.stderr);
          elif arguments.format == "md" and dataset not in flats:
            #
            # Markdown table with summary statistics
            #
            with open(os.path.join(dataset, "counts", part, "source.json")) as _:
              s = json.load(_)["tokens"];
            with open(counts) as _: r = json.load(_)["tokens"];
            t = len(glob.glob(os.path.join(release, "*.jsonl.zst")));
            print("| `{}` | {} | {:,} | {:,} | {:,.1f} | {} |"
                  "".format(dataset, f"`{part}`" if not flat else "",
                            s, r, r / s * 100, t));
            if flat: flats.add(dataset);
          if not os.path.isdir(tokens):
            print("plan.py(): no .megatron-lm. directory for {}."
                  "".format(dataset + "/" + part), file = sys.stderr);
          elif not os.path.isfile(checksums):
            print("plan.py(): no .megatron-lm. checksums for {}."
                  "".format(dataset + "/" + part), file = sys.stderr);
          elif os.path.getmtime(tokens) > os.path.getmtime(checksums):
            print("plan.py(): out-of-date .megatron-lm. checksums for {}."
                  "".format(dataset + "/" + part), file = sys.stderr);
          else:
            i = len(glob.glob(os.path.join(tokens, "*.info.json")));
            i += len(glob.glob(os.path.join(tokens, "*_text_document.bin")));
            i += len(glob.glob(os.path.join(tokens, "*_text_document.idx")));
            with open(checksums, "rb") as stream:
              j = sum(1 for _ in stream);
            if i != j:
              print("plan.py(): mismatch ({} vs. {}) in .megatron-lm. checksums for {}."
                    "".format(i, j, dataset + "/" + part), file = sys.stderr);
              
  if arguments.budget:
    if arguments.format == ",":
      print("dataset,part,budget,usage"
            ",source tokens,source documents,source length"
            ",sample tokens,sample documents,sample length"
            ",token reduction,document reduction");
    for path, data in mix.items():
      if not data["active"]: continue;
      counts = data["counts"];
      if "source" not in counts and "openeurollm" not in counts:
        if not arguments.quiet:
          print("plan.py(): no .source. counts for {} (#{})."
                "".format(path, i),
                file = sys.stderr, flush = True);
        continue;
      source = counts["openeurollm"] if "openeurollm" in counts else counts["source"];
      sample = counts["sample"] if "sample" in counts else None;
      tokens = source["tokens"] if sample is None else sample["tokens"];
      documents = source["documents"] if sample is None else sample["documents"];
      budget = math.ceil(arguments.horizon * data["ratio"] / 1e6);
      pool = math.floor(tokens / 1e6);
      percent = budget / pool * 100;
      if arguments.format == "plain":
         print("{}:{}: {:,}m tokens of {:,}m ({:,.1f}%)."
               "".format(data["dataset"], data["part"], budget, pool, percent));
      elif arguments.format == "yaml":
        print("  {}:".format(data["part"]));
        #
        # per suggestion by @spyysalo, aim for shards around 100b tokens
        #
        shard = 1e11 / (tokens / documents);
        if shard > 1e6: shard = "{}md".format(round(shard / 1e6));
        elif shard > 1e3: shard = "{}kd".format(round(shard / 1e3));
        else: shard = "{}d".format(round(shard));
        percent = math.ceil(percent);
        if percent >= 100:
          print(f"    sample: full\n    shard: {shard}");
        else:
          print("    sample: random\n    budget: {}%\n    shard: {}"
                "".format(percent, shard));
      elif arguments.format == "sample":
        if sample is None: continue;
        print("{}:{}: {:,}m source tokens |{:,.1f}|; "
              "{:,}m sample tokens |{:,.1f}| "
              "({:,.1f}%)."
              "".format(data["dataset"], data["part"],
                        source["tokens"] // 1e6,
                        source["tokens"] / source["documents"],
                        sample["tokens"] // 1e6,
                        sample["tokens"] / sample["documents"],
                        sample["tokens"] / source["tokens"] * 100));
      elif arguments.format == ",":
        budget = math.ceil(arguments.horizon * data["ratio"]);
        print("{},{},{},{:.3f}"
              ",{},{},{:.1f}"
              "".format(data["dataset"], data["part"], budget, budget / tokens,
                        source["tokens"], source["documents"],
                        source["tokens"] / source["documents"]),
              end = "");
        if sample is None:
          print(",,,,,");
        else:
          print(",{},{},{:.1f}"
                ",{:.3f},{:.3f}"
                "".format(sample["tokens"], sample["documents"],
                          sample["tokens"] / sample["documents"],
                          sample["tokens"] / source["tokens"],
                          sample["documents"] / source["documents"]));
    sys.exit(0);

  if arguments.finepdfs:
    for path, data in mix.items():
      if path.startswith("finepdfs-1.0.0"):
        edu = path.replace("finepdfs-1.0.0", "finepdfs-edu-1.0.0");
        if edu not in mix:
          print("{:,.6f} {}".format(data["ratio"], path));
          continue;
        n = data["ratio"] + mix[edu];
        _ = os.path.join(edu.replace("/megatron-lm", "/counts"), arguments.counts)
        with open(_, encoding = "utf-8") as _:
          r = min(n, json.load(_)["tokens"] / arguments.horizon);
          print("{:,.6f} {}".format(r, edu));
          if n > r: print("{:,.6f} {}".format(n - r, path));
    sys.exit(0);
    

if __name__ == "__main__":
  main();
