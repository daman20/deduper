#Bundles the Helper scripts together
import deletedupes, makehashes, os
directory = "."
for i in [x[0] for x in os.walk(directory)]:
  makehashes.main(i)
deletedupes.main()