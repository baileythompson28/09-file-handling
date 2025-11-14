import os 
#listing files in a directory

directory_path = "./" #our current directory
all_files = os.listdir(directory_path) #returns files AND folders
print(f"All entries: {all_files}")

#get only files:
#use list comprehension
#for each elements if it is a file
# give me the thing, if the thing in all things meets the condition
files_only = [file for file in all_files if os.path.isfile(
    os.path.join(directory_path, file))]
print(files_only)

#get specific files
csv_files = [file for file in all_files if os.path.isfile(
    os.path.join(directory_path, file)) and file.endswith(".csv")]
print(csv_files)

#see if file or folder exists:
target_file_path = "fake file.csv"
if os.path.exists(target_file_path):
    print(f"The file ('{target_file_path}') was found")
else:
    print(f"The file ('{target_file_path}') was NOT found")

#see if the file is a file (not a folder)
if os.path.isfile(target_file_path):
    print(f"The file ('{target_file_path}) is a file")
else:
    print(f"The file ('{target_file_path}) is NOT a file")