# folders.py #
import os 
import re 

# We use mimetypes module to extract all available file types,
# it will stored in a dictionary and return from a function to
# access in the main script of the program.
import mimetypes

# Folders
FOLDERS = ['Others', 'Music', 'Pictures', 'Documents',  'Documents', 'Videos']

# Check for existing folders. 
# Useful for non-english idiom os versions 
# os that doesn't have this folders. 
def init():
    for folder in FOLDERS:
        if not os.path.exists(os.path.join(os.path.expanduser('~'), folder)):
            os.makedirs(os.path.join(os.path.expanduser('~'), folder))

# Folder to be sent
def getfolder(file_to_folder):
    return folder_to[file_to_folder]

# Regex to match in available types
types = re.compile(r'[a-z]+')

# Store all in a list
file_types = [types.search(i).group() for i in mimetypes.types_map.values()]

# Simplify list
file_types = set(file_types)
file_types = list(file_types)
file_types.sort()

# final dictionary to track folders
#
#    Type   and  folder 
#    
#    'audio' :   Music
#    'image' :   Pictures
#    'video' :   Videos
#     -
#     -

folder_to = {file_types[i] : FOLDERS[i] for i in range(0, len(FOLDERS))}



