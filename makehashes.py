import hashlib
from os import listdir
from os.path import isfile, join
import os
import json

import guifunctions
from guifunctions import *

def getListOfFiles(dirName):
  # create a list of file and sub directories
  # names in the given directory
  listOfFile = os.listdir(dirName)
  allFiles = list()
  # Iterate over all the entries
  for entry in listOfFile:
    # Create full path
    fullPath = os.path.join(dirName, entry)
    # If entry is a directory then get the list of files in this directory
    if os.path.isdir(fullPath):
      allFiles = allFiles + getListOfFiles(fullPath)
    else:
      allFiles.append(fullPath)

  return allFiles

def sha512(fname):
    hash_sha = hashlib.sha512()
    if(fname != "hashes.json"):
      with open(fname, "rb") as f:
          for chunk in iter(lambda: f.read(2 ** 20), b""):
              hash_sha.update(chunk)
    return hash_sha.hexdigest()
def main(filenames):
  hashes = {}
  for filename in filenames:
    print(f"Now Calculating : {filename}")
    hashes[filename] = sha512(filename)
  return hashes
def realmain(directory):
    return main(getListOfFiles(directory))