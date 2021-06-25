import json, os
from guifunctions import *
def main():
  print("Commencing Deleting")
  f = open('hashes.json', 'r')
  hashes = json.load(f)

  rev_dict = {}
  for key, value in hashes.items():
      rev_dict.setdefault(value, set()).add(key)
    
    
  result = filter(lambda x: len(x)>1, rev_dict.values())
  oktextui(f"The following files have the same contents: {list(result)}", "Same Content Files")
  for i in list(result):
    if(i != "main.py" or i != "deletedupes.py" or i != "makehashes.py" or i != "requirements.txt"):
      os.remove(i)
  print("We sucessfully removed the duplicate files")
  print("Cleaning Up")
  os.remove("hashes.json")