#!/usr/bin/env python

# -*- coding: utf-8; -*-

import argparse;
from functools import cmp_to_key;
import glob;
import io;
import json;
import math;
from operator import itemgetter;
import os;
import re;
import sys;
import time;

def main():

  #
  # helper function to sort shard names by BSC-edu score levels
  #
  def cmp(left, right):
    left = left[-len("??.info.json"):];
    right = right[-len("??.info.json"):];
    if left < right: return -1;
    elif left > right: return 1;
    else: return 0;

  start = time.time();

  parser = argparse.ArgumentParser(description = "Optimize BSC-edu Scores for HPLT 4.0");
  parser.add_argument("--root", type=str, default="/scratch/project_465002530/training/collection");
  parser.add_argument("--horizon", type = lambda _: int(float(_)), default = 3e12);
  parser.add_argument("--calibrate", type = lambda _: float(_), default = 1);
  parser.add_argument("--quiet", action = "store_true", default = False);
  parser.add_argument("inputs", nargs = "+");
  arguments = parser.parse_args();

  clean = {"name": "clean"}; noisy = {"name": "noisy"};
  with open(arguments.inputs[0], encoding = "utf-8") as stream:
    for i, line in enumerate(stream):
      line = line.strip();
      path, count = line.split(",");
      if path.startswith("./"): path = path[2:];
      fields = path.split("/");
      if len(fields) > 3: continue;
      _ = len(".info.json");
      bucket = int(fields[2][-(_ + 2):-_]);
      map = clean if fields[0] == "clean" else noisy;
      entry = {"partition": fields[0], "language": fields[1], "bucket": bucket, "n": int(count), "paths": [path]};
      if fields[1] not in map: map[fields[1]] = [entry];
      else: map[fields[1]].append(entry);
  for map in (clean, noisy):
    name = map.pop("name");
    for entries in map.values():
      entries.sort(key = itemgetter("bucket", "n"));
      i = 0;
      while i < len(entries) - 1:
        if entries[i]["n"] < 150000:
          _ = entries[i + 1];
          _["n"] += entries[i]["n"];
          _["paths"] += entries[i]["paths"];
          entries[i].pop("paths");
        i += 1;
      #
      # finally, if need be, also merge downwards from the top
      #
      i = len(entries) - 1;
      while i > 0:
        if entries[i]["n"] < 150000 and "paths" in entries[i]:
          j = 1;
          _ = entries[i - j];
          while not "paths" in _ and i >= j:
            j += 1;
            _ = entries[i - j];
          if "paths" in _:
            _["n"] += entries[i]["n"];
            _["paths"] += entries[i]["paths"];
            entries[i].pop("paths");
        i -= 1;
    for language in sorted(map.keys()):
      for entry in map[language]:
        if "paths" in entry and len(entry["paths"]) > 1:
          print(entry);
      

if __name__ == "__main__":
  main();
