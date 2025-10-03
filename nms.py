import os
import shutil
from datetime import datetime

d = datetime.now()

nms_folder_location = os.path.expandvars(r'%APPDATA%\HelloGames\NMS')

#Change this. This is your user folder. It is found in %APPDATA%\HelloGames\NMS
usr_folder = "st_76561198014040903"

#Change this. Specify a location where the backups are to be saved.
destination_folder_location = r'C:\Backups\NMS'

destination_subfolder = d.strftime('%d-%m-%y')

path_copy = os.path.join(nms_folder_location, usr_folder)

full_backup_path = os.path.join(destination_folder_location, destination_subfolder)
copy_destination = ""

#Create day based folder
try:
    os.mkdir(full_backup_path)
except FileNotFoundError:
    print('Backup root folder not found')
except FileExistsError:
    print('Folder already exists. Creating a subfolder for new backups.')

#Create time based subfolder
try:
    copy_destination = os.path.join(full_backup_path, (d.strftime('%H%M')))
    os.mkdir(copy_destination)
except FileNotFoundError:
    print('Backup root folder not found')
except FileExistsError:
    copy_destination = os.path.join(full_backup_path, (d.strftime('%H%M-%S')))
    os.mkdir(str(copy_destination))

#Copy folder
try:
    shutil.copytree(path_copy, copy_destination, dirs_exist_ok=True)
except:
    print('Error copying folder to backup destination.')
else:
    print('New backups are created!')