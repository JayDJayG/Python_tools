import os
from datetime import datetime



os.chdir('C:/Users/Jairo Guzman/Desktop')

#Shows directory tree: directory tree, directory list, and the files within the path

'''
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print ('current path:', dirpath)
    print ('directories:', dirnames)
    print ('Files:', filenames)
    print()

'''
#Print environment variables
print(os.environ.get('HOME'))
#add a certain file, or location to the environment variable
#file_path = os.path.join(os.environ.get('HOME'), 'whatever.txt')
