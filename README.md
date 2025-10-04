# nms-save-backup-py

Script to take local backups of No Man's Sky saves.

## Description

A simple Python script to take backups of No Man's Sky saves. The backups are saved locally. 

You only need to update your user profile folder name (e.g. "st_123452323452") in the script. If you want to save your backups in a different location, then you only need to update "destination_folder_location" variable.

Backups are saved in C:\Backups\NMS\\{date}\\{hourminute} folder. For example, C:\Backups\NMS\04-10-25\1507. In cases where a folder named 1507 would exist, then a new folder is created with seconds as suffix, e.g. 1507-45.
This way you can take multiple backups if it's needed.

## Getting Started

### Dependencies

* Windows
* Python installed
  
### Installing

* git clone or save the nms.py file locally
* Edit variable "usr_folder" in nms.py to match your user profile folder in %APPDATA%\HelloGames\NMS
* You can reach the folder example with WIN + R and type %APPDATA%\HelloGames\NMS
* You will see a folder that's something like "st_123452323452". Copy the folder name and update "usr_folder" in nms.py.

### Executing program

* python nms.py
