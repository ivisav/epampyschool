import os

# Create dir, move there, create empty file
os.mkdir('new_dir')
os.chdir('new_dir')
open('new_file.txt', 'a').close()

# Write to file
with open('new_file.txt', 'w') as file:
    for i in range(5):
        file.write(f"Hello World! {i} \n")

# Read from file
with open('new_file.txt', 'r') as file:
    for line in file.readlines():
        print(line)

# Rename file new_file.txt -> new_name_file.txt
os.rename('new_file.txt', 'new_name_file.txt')


"""
(!!) Remember! Running this script for the second time will raise an error:
FileExistsError: [Errno 17] File exists: 'new_dir'
If you want to avoid it - you need to check if dir / file already exists 
"""