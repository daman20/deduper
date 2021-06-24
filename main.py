#Bundles the Helper scripts together
import deletedupes, makehashes, os
directory = "."
def hashing(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir and not str(it.path).startswith("."):
            makehashes.main(it.path)
            hashing(it)
 
hashing(directory)
deletedupes.main()