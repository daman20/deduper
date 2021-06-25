import json, os
def main():
  print("Commencing Deleting")
  with open('hashes.json', 'r') as file:
    hashes = json.loads(file.read())

  rev_dict = {}
  for key, value in hashes.items():
      rev_dict.setdefault(value, set()).add(key)
    
    
  result = filter(lambda x: len(x)>1, rev_dict.values())
  print(f"The following files have the same contents: {list(result)}")
  for i in list(result):
    if(i != "main.py" or i != "deletedupes.py" or i != "makehashes.py" or i != "requirements.txt"):
      os.remove(i)
  print("We sucessfully removed the duplicate files")
  print("Cleaning Up")
  os.remove("hashes.txt")