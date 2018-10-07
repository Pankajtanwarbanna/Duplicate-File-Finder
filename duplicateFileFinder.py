import os
import sys
import hashlib
import time

def hashfile(path,blocksize=65536):
    hasher = hashlib.md5()
    file = open(path,"rb")
    buf = file.read(blocksize)
    while(len(buf)>0):
        hasher.update(buf)
        buf = file.read(blocksize)
    file.close()
    return hasher.hexdigest()

def findDups(parentFolder):
    p = 0
    dups = {}
    print("%s scanning.............."%a)
    for dirName, subdirs,fileList in os.walk(parentFolder):
        for filename in fileList:
            path = os.path.join(dirName,filename)
            file_hash = hashfile(path)
            if file_hash in dups:
                p = p+1
                print("Duplicate file "+str(p)+" - " + filename)
                print("file path - "+ path)
                dups[file_hash].append(path)
            else :
                dups[file_hash]= [path]
    return p
a = input("Enter local disk name to scan!\n").upper()
p = findDups("%s:/"%a)
print("Scan Completed!")
if(p==0):
    print("No duplicate file found in local disk "+a)
time.sleep(15)




    










    
                
            
