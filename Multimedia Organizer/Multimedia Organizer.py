## Multimedia Organizer ##

# This is a simple multimedia file organizer's.
# The program consists in send the commom file types
# to the user root folder (Pictures, Video, Music...)

# As first step we need to specify the path to be scanned
# after that, our application will send the files to the directories

import re 
import sys 
import shutil
import os 

import mimetypes
import folders as f

# init
f.init()

# user root folder to send files to the folders
USER_DIRECTORY = os.path.expanduser("~")

# folder to be scanned by our Multimedia Organizer
# if is not specified, the program will take user root directory by default. 
SCANN_FOLDER = USER_DIRECTORY

# check the user input 
try:
	SCANN_FOLDER = sys.argv[1]

except IndexError:
	pass

# if it fails, the progam exits 
if not os.path.exists(SCANN_FOLDER):
	exit('Please specify an existing directory.\n')

# set directory to be scanned 
os.chdir(SCANN_FOLDER)

# get the file type compare and add to the file_name list
file_names = [i for i in os.listdir('.') if os.path.isfile(i)]

# regex pattern to identify files.
types = re.compile(r'[a-z]+')

# moved files
success_moved = []

# check for each file and perfom operations to move
for file in file_names:
	if types.search(str(mimetypes.guess_type(file))).group() == 'one':
		continue

	# move the file to the corresponding folder
	try:
		shutil.move(file, os.path.join(USER_DIRECTORY, f.getfolder(types.search(str(mimetypes.guess_type(file))).group())))	 
	
	# if the file already exists then delete it.
	except:
		os.remove(os.path.join(USER_DIRECTORY, f.getfolder(types.search(str(mimetypes.guess_type(file))).group()), file))

	success_moved.append(file)

# print files
print('Modified files:\n')
for i in success_moved:
	print(i) 

