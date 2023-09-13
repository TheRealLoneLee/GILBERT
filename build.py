import os
import zipfile
import shutil
from tqdm import tqdm

# Check if the directory "builds" exists
if not os.path.exists("builds"):
    os.makedirs("builds")

# Ask the user for the current version
version = input("Please enter the current version in the format 'v0.0.0': ")

# Define the .zip file name
zipfile_name = "Gilbert-" + version + ".zip"

# Create a ZipFile object
with zipfile.ZipFile(os.path.join("builds", zipfile_name), 'w') as zipf:
    # List of files to add
    files_to_add = ["./automation-tools/setup.py", "./automation-tools/initiate.sh"]

    # Iterate over each file
    for file in tqdm(files_to_add, desc="Zipping files", unit="file"):
        # Check if the file exists
        if os.path.exists(file):
            # Add file to the .zip file
            zipf.write(file)
        else:
            print(f"{file} does not exist in the current directory.")
