import os

# Specify the directory you want to list. Use '.' for current directory.
directory = '.'

# Get the list of files and directories
contents = os.listdir(directory)

# Print each entry in the directory
for item in contents:
    print(item)