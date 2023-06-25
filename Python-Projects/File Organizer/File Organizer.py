# File Organizer

import os
import shutil

def organize_files(directory):
    # Create a dictionary to map file extensions to folder names
    extensions = {
        '.txt': 'Text Files',
        '.docx': 'Word Documents',
        '.xlsx': 'Excel Files',
        '.jpg': 'Image Files',
        '.png': 'Image Files',
        '.pdf': 'PDF Files'
    }

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # Get the file extension
            _, file_ext = os.path.splitext(filename)
            
            # Check if the extension is in the dictionary
            if file_ext.lower() in extensions:
                # Create the destination folder if it doesn't exist
                dest_folder = os.path.join(directory, extensions[file_ext.lower()])
                os.makedirs(dest_folder, exist_ok=True)
                
                # Move the file to the destination folder
                src_file = os.path.join(directory, filename)
                dest_file = os.path.join(dest_folder, filename)
                shutil.move(src_file, dest_file)

    print("File organization complete.")

# Test the file organizer
directory = input("Enter the directory path: ")
organize_files(directory)


'''
=================================
Test Case:
=================================

Enter the directory path: C:\Projects-with-Pawar-Codes\Python-Projects\File Organizer
File organization complete.


# Dir before:
file1.txt
file2.docx
file3.jpg
file4.pdf

# Dir after:
Text Files
  - file1.txt
Word Documents
  - file2.docx
Image Files
  - file3.jpg
PDF Files
  - file4.pdf



'''