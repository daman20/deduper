#Bundles the Helper scripts together
import deletedupes, makehashes, os, json, guifunctions

if os.path.exists("/appdata/hashes.json"):
  os.remove("/appdata/hashes.json")
directory = "/scan"
guifunctions.oktextui(f"The program is currently hashing", "Hashing")
hashes = makehashes.realmain(directory)
with open("/appdata/hashes.json", "a+") as myfile:
  print(myfile)
  myfile.write(json.dumps(hashes))
  myfile.close()
guifunctions.oktextui("Hashing Complete", "Completed Hashing")
deletedupes.main()