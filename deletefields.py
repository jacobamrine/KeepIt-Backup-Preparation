#Jacob Amrine 6/14/22
#When downloading zip files of SharePoint backups from Keepit, for some reason
#it creates a copy of every file, with a "Fields" in the file extension. This
#file, as far as I know, doesnt actually contain any data.
#
#This script deletes all files ending in " Fields" in the directory it was run from, and recursively through sub directories
#
#WARNING: This program is destructive and deletes with no remorse! Keep a backup of your files and run at your own risk!
#You can test for the files it will delete by commenting out the os.remove line, and viewing the output

import os

for root, dirnames, filenames in os.walk(os.getcwd()): #os.walk recurses through directories
    for filename in filenames:
        if filename.endswith(" Fields"):
            print("File Name: " + filename)
            #os.remove(os.path.join(root,filename)) #Joins to find the full file path, then gets deleted!
print("Done!")
