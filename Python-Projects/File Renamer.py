# File Renamer

import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            new_filename = filename.replace(" ", "_")  # Modify the renaming logic as needed
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed file: {filename} -> {new_filename}")

# Test the File Renamer
directory = input("Enter the directory path: ")
rename_files(directory)
