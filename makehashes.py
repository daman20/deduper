import hashlib
from os import listdir
from os.path import isfile, join
import os
import json

def sha512(fname):
    hash_sha = hashlib.sha512()
    if(fname != "hashes.txt"):
      print(f"{fname} is being delted if necessary")
      with open(fname, "rb") as f:
          for chunk in iter(lambda: f.read(2 ** 20), b""):
              hash_sha.update(chunk)
    return hash_sha.hexdigest()
def main(mypath):
  hashes = {}
  filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  print(mypath)
  for filename in filenames:
    print(f"Now Calculating : {filename}")
    hashes[filename] = sha512(filename)
  with open("hashes.txt", "a+") as myfile:
    print(hashes)
    myfile.write(json.dumps(hashes))
    myfile.close()
  print("Hashing Complete")
