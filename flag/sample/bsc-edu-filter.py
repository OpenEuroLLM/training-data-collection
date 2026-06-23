import json;
import sys;

def sample(document, parameters):
  threshold = parameters.get("threshold", 1.5);
  if "bsc-edu" in document and document["bsc-edu"] < threshold:
    return 0;
  return 1;

def main():
  for line in sys.stdin:
    _ = json.loads(line.strip());
    _["score"] = sample(_, {"threshold": 1.5});
    print(json.dumps(_));
        
if __name__ == "__main__":
 main();

