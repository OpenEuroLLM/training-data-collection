#!/usr/bin/env python

# -*- coding: utf-8; -*-

#
# rclone --config ~/rclone.conf lsjson \
#   --recursive --files-only --no-mimetype --hash \
#   lumi-465002530-private:baby-collection \
# | ./etc/manifest.py > manifest.json
#
# grep /release/ manifest.json | ./etc/manifest.py --md > urls.md
#

import argparse;
import json;
import sys;

def main():

  parser = argparse.ArgumentParser(description = "Creation and Formatting of Download Manifest");
  parser.add_argument("--md", action = "store_true", default = False);
  arguments = parser.parse_args();

  if arguments.md:
    print("| **URL** | **Size** |\n"
          "|---------|------- --|");
    for line in sys.stdin:
      _ = json.loads(line.strip());
      print("| [`{}`]({}) | {:,} |"
            "".format(_["url"], _["url"], _["size"]));
    return 0;
  
  for _ in json.load(sys.stdin):
    path = _["Path"];
    size = _["Size"];
    mtime = _["ModTime"];
    md5 = _["Hashes"]["md5"];
    json.dump({"url": f"https://data.openeurollm.eu/prelude/baby/{path}",
               "bucket": "baby-collection", "path": path,
               "size": size, "mtime": mtime, "md5": md5},
              sys.stdout, indent = None);
    print();

if __name__ == "__main__":
  main();
