import os
import shutil
import datetime
import schedule
import time

source_dir = "C:\Users\abhi\\OneDriv\\Picture\\Screenshots"
destination_dir = "D:\Ad\\Cod\\Githu\\Automated File Backup\Destination Dir"

def copy_folder_to_dir(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, today.str(today))

    try :
        shutil.copytree(source, dest_dir)
        print(f"Folder copied successfully to {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in {dest_dir}")
