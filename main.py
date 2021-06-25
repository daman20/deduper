#Bundles the Helper scripts together
import deletedupes, makehashes, os
directory = "."
allsubdirs = list_subfolders_with_paths = [f.path for f in os.scandir(directory) if f.is_dir()]
for i in allsubdirs:
  print(i)
  makehashes.main(i)
deletedupes.main()