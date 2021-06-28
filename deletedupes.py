import json
import os

import guifunctions
from guifunctions import *


def main():
    guifunctions.oktextui("Commencing Deleting", "Commencing Deleting")
    f = open('/appdata/hashes.json', 'r')
    hashes = json.load(f)

    rev_dict = {}
    for key, value in hashes.items():
        rev_dict.setdefault(value, set()).add(key)

    result = filter(lambda x: len(x) > 1, rev_dict.values())
    layout = [
        [sg.Text('Select which duplicates you would like deleted')],
        [sg.Checkbox(text, 1) for text in list(result)],
        [sg.Button('Done')]
    ]

    window = sg.Window('Duplicate Selector', layout, finalize=True)
    print("created deletedupe window")
    dupestobedeleted = []
    while True:  # Event Loop
        event, values = window.Read()
        if event is None or "Done":
            print(f"EVENT IS: {event} \n VALUES IS: {values}")
            break
        window.close()
        print(values)
        numberstobedeleted = [v for k, v in dict(values).items() if v['True']]
        for i in numberstobedeleted:
          filetobedeleted = list(result)[i]
          print(filetobedeleted)
          dupestobedeleted.append(filetobedeleted)
    print(f"Dupes to be deleted is {dupestobedeleted}")
    for i in dupestobedeleted:
        if i != "main.py" or i != "deletedupes.py" or i != "makehashes.py" or i != "requirements.txt":
            os.remove(i)
    oktextui("We sucessfully removed the duplicate files", "Dupes Deleted")
    print("Cleaning Up")
    os.remove("/appdata/hashes.json")
