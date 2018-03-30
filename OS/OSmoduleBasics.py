import os
from datetime import datetime

#print current directory
print(os.getcwd())

#Change the directory

os.chdir('C:/Users/Jairo Guzman/Desktop')
print(os.getcwd())

#List the files in a directory
print(os.listdir())

#to make a dir os.mkdir('MyDirectory'), os.makedirs('MyDirectory/MyDirectory2')
#to remove a dir os.rmdir('MyDirectory'), os.removedirs('MyDirectory/MyDirectory2') is recursively
#to rename a file os.rename('MyDirectory.txt', 'MyNewDirectoryName.txt'),

#to see the stats of a file
print(os.stat('Adjustment of Status'))

#to see the stats.size of a file
print(os.stat('Adjustment of Status').st_size)

#human readable las time of modification
mod_time = os.stat('Adjustment of Status').st_mtime
print(datetime.fromtimestamp(mod_time))
