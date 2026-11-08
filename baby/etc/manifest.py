#!/usr/bin/env python

# -*- coding: utf-8; -*-

#
# rclone --config ~/rclone.conf lsjson \
#   --recursive --files-only --no-mimetype --hash \
#   lumi-465002530-private:baby-collection \
# | ./etc/manifest.py > manifest.json
#

import json;
import sys;

def main():

  for _ in json.load(sys.stdin):
    path = _["Path"];
    size = _["Size"];
    mtime = _["ModTime"];
    md5 = _["Hashes"]["md5"];
    json.dump({"bucket": "baby-collection", "path": path,
               "size": size, "mtime": mtime, "md5": md5,
               "url": f"https://data.openeurollm.eu/prelude/baby/{path}"},
              sys.stdout, indent = None);
    print();

if __name__ == "__main__":
  main();
