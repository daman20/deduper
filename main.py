#Bundles the Helper scripts together
import deletedupes, makehashes, os, json
directory = "/scan"
allsubdirs = list_subfolders_with_paths = [f.path for f in os.scandir(directory) if f.is_dir()]
for i in allsubdirs:
  print(i)
  hashes = makehashes.main(i)
with open("hashes.json", "a+") as myfile:
  print(hashes)
  myfile.write(json.dumps(hashes))
  myfile.close()
print("Hashing Complete")
deletedupes.main()