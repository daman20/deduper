#Bundles the Helper scripts together
import deletedupes, makehashes, os, json, guifunctions


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

if os.path.exists("/appdata/hashes.json"):
  os.remove("/appdata/hashes.json")
directory = "/scan"
allsubdirs = getListOfFiles(directory)
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