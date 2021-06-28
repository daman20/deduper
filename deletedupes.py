import json, os
import PySimpleGUI as psg
import guifunctions
from guifunctions import *
def main():
  guifunctions.oktextui("Commencing Deleting", "Commencing Deleting")
  f = open('/appdata/hashes.json', 'r')
  hashes = json.load(f)

  rev_dict = {}
  for key, value in hashes.items():
      rev_dict.setdefault(value, set()).add(key)
    
    
  result = filter(lambda x: len(x)>1, rev_dict.values())
  layout = [
    [sg.Text('Select which duplicates you would like deleted')],
    [sg.Checkbox(text, 1) for text in list(result)],
    [sg.Button('Done')]
  ]

  window = sg.Window('Duplicate Selector', layout)

  while True:  # Event Loop
    event, values = window.Read()
    if event is None:
      break
    print(values)
    dupestobedeleted = []
    for ele in values:
      if not values[ele]:
        dupestobedeleted.append(ele)
  for i in dupestobedeleted:
    if(i != "main.py" or i != "deletedupes.py" or i != "makehashes.py" or i != "requirements.txt"):
      os.remove(i)
  oktextui("We sucessfully removed the duplicate files", "Dupes Deleted")
  print("Cleaning Up")
  os.remove("hashes.json")
  oktextui("Dupes Successfully Deleted", "Deduping Complete")