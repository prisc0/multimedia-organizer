# Multimedia organizer 
&nbsp; Simple media files organizer based on mime-types.

## Description

&nbsp; Multimedia Organizer allow us to organize our multimedia files in a determined folder, the files are sent to the user root folder, ex. on Windows 'C:\\Users\\USER_PATH\\...' and organize in the corresponding folder (Videos, Music, Documents...) .

![INTRO IMAGE](Multimedia Organizer/githubimg.gif)<br/>


## Common issues
&nbsp; In this project, one of the common issues is the recognition of the file extension/type and here is where mime-type get in action, instead of use a large pattern in a dictionary or another third-party library to help for to get the file format.   

A short example could be:

>>> import mimetypes
>>>
>>> mimetypes.guess_type('some_media_file.mp3')
>>> ('audio/mpeg', None)

# Requirements
&nbsp; python3.x
&nbsp; send2trash (optional)

# Instructions

Windows
python3.x Multimedia Organizer.py 'C:\\Users\\USER_PATH\\some_folder\\..files..

Linux
python3.x Multimedia Organizer.py /home/user/folder/..files..

Notice that the only changes is the back and forward slashes (our program internally solve it)

# Errors
&nbsp; Possible erros can be generate when we have repeated files on the folder (a double call to the script will delete it).
