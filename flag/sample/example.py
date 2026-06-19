#
# plug-ins to Training Data Packer, annotation-based filtering and resampling.
# this file provides a set of procedures that each take a document as input and
# return a float in the interval [0, 4]
#

import random;

def sample(document, documents, tokens):
  return random.uniform(0, 4);
