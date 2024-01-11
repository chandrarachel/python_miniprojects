# Performs multiple types of file organizations based on the user's input, including:
# 1. Organize files according to their types (png, pdf, pptx, etc).
# 2. Delete files if their names include a user-specified word: If any file's name contains the word, the file will be deleted.
# 3. Change filenames it they include a user-specified word: If any file's name contains the word, the filename will be changed according to the user's input (example: change filename including '2012' into 'oldPhotos').

import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            if word_delete in filename:
                os.remove(file_path)
            elif fname_change in filename:
                new_file_path = file_path.replace(fname_change, inp_new_filename)
                os.rename(file_path, new_file_path)
            else:
                file_type = filename.split(".")[-1]
                target_directory = os.path.join(directory, file_type.upper() + " Files")
                os.makedirs(target_directory, exist_ok=True)
                target_path = os.path.join(target_directory, filename)
                shutil.move(file_path, target_path)


directory_path = input("Enter the directory path to organize: ")
word_delete = input("Remove file(s) if its name includes: ")
fname_change = input("Change filename(s) if it includes: ")
inp_new_filename = input("Enter the new filename: ")
organize_files(directory_path)