from sys import *
import hashlib
import os

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb') 
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def DisplayChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isabs(path)
    if exists:
        for dirName, dubdir, filenames in os.walk(path):
            print("Current Folder is :"+dirName)
            for file in filenames:
                path = os.path.join(dirName, file)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')

def main():

    print("_____________Pradnya Dolthade__________________")

    print("Application name : "+argv[0])

    if(len(argv) != 2):
        print("Error : Invalid number of arguments.")
        exit()

    if(argv[1] == "-h") or (argv[1]=="-H"):
        print("This script is used to traverse specific directory and display checksum of files")
        exit()

    if(argv[1] == "-u") or (argv[1]=="-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extention ")
        exit()

    try:
        arr = DisplayChecksum(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)
                                                        
if __name__ == "__main__":
    main()

