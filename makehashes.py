import hashlib
from os import listdir
from os.path import isfile, join
import os
import json

import guifunctions
from guifunctions import *

def sha512(fname):
    hash_sha = hashlib.sha512()
    if(fname != "hashes.json"):
      with open(fname, "rb") as f:
          for chunk in iter(lambda: f.read(2 ** 20), b""):
              hash_sha.update(chunk)
    return hash_sha.hexdigest()
def main(mypath):
  hashes = {}
  filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  for filename in filenames:
    print(f"Now Calculating : {filename}")
    currentfile = f"{mypath}/{filename}"
    hashes[currentfile] = sha512(currentfile)
    return hashes
