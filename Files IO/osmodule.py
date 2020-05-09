import os

print(os.getcwd()) # prints path of this file

#os.makedirs('Day6') # creates folder

print(os.path.abspath('.\\pythoncodes'))

print(os.path.dirname('c:\\pythoncodes\\Day6')) # it prints directory name of Day6

print(os.path.getsize('c:\\pythoncodes\\Pyhtonobjects.py')) # prints size in bytes

print(os.path.isfile('c:\\pythoncodes\\PyhtonObjects.py')) #will return true if it is a file

print(os.path.isdir('c:\\pythoncodes\\Day6')) # will return true if it is a directory

#os.unlink('c:\\pythoncodes\\testfile.txt') # deletes file

os.rmdir('c:\\pythoncodes\\Day6')


    
