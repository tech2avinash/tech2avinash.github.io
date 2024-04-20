# Install the filesplit module (if not already installed)
# You can do this using pip:
# pip install filesplit

from filesplit.split import Split
from filesplit.merge import Merge

# Create an instance for splitting
split = Split(inputfile="models/func/functionary-small-v2.4.Q4_0.gguf", outputdir="models/func/chunks")

# Split the file by a specified size (e.g., 10 MB)
#split.bysize(size=1024 * 1024 * 1024)  # 10 MB in bytes

# Create an instance for merging
merge = Merge(inputdir="models/func/chunks", outputdir="models/func/merged", outputfilename="functionary-small-v2.4.Q4_0.gguf")

# Merge the split files back into one
merge.merge()

# The merged file will be saved as "merged_file.txt"
