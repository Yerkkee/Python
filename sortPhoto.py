import glob
import os.path, time
import datetime
import shutil
import os


# File location, folder
dir_file = r'C:\Users\blablalba\bla'

# All file formats
ext = ['png', 'jpg', 'gif', 'jpeg', 'avi', 'mp4', 'mov', 'wmv', 'mkv']

# Cycle to check each format
listFile = []
[listFile.extend(glob.glob(dir_file + "\*." + e)) for e in ext]

# Loop to check each file 
for i in listFile:
    path = ""
    # General file data (when it was changed)
    file_date = time.ctime(os.path.getmtime(i))
    file_date = datetime.datetime.strptime(file_date, "%a %b %d %H:%M:%S %Y")

    year_file = file_date.strftime('%Y') # Takes the year change from the file
    month_file =file_date.strftime('%m') # Takes month change from file
    path = os.path.join(dir_file, year_file)
    path = os.path.join(path, month_file)
    os.makedirs(path, exist_ok=True) # Creates a folder if not
    shutil.move(i, path) # Expression can be changed to shutil.copy (i, path) then it will copy


print("The End!")