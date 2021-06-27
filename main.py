#Bundles the Helper scripts together
import deletedupes, makehashes, os, json, guifunctions
directory = "/scan"
allsubdirs = list_subfolders_with_paths = [f.path for f in os.scandir(directory) if f.is_dir()]
guifunctions.oktextui(f"The program is currently hashing", "Hashing")
for i in allsubdirs:
  print(i)
  hashes = makehashes.main(i)
with open("/appdata/hashes.json", "a+") as myfile:
  print(myfile)
  myfile.write(json.dumps(hashes))
  myfile.close()
guifunctions.oktextui("Hashing Complete", "Completed Hashing")
deletedupes.main()