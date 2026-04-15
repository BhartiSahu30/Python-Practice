import os

#specify the directory want to list
directory_path = '/'
#list all files and directiories in specified path
contents = os.listdir(directory_path)

#print each files and directory name
"""for item in contents:
    print(item)"""
print(contents)