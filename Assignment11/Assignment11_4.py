
from sys import *
import hashlib
import os
import time

def ProcessDisplay(dict1, log_dir = "Log.txt"):
    

    separator = "*" * 80
    f = open(log_dir,'w')
    f.write(separator+'\n')
    f.write('Process Logger :'+time.ctime()+"\n")
    f.write(separator+'\n')
    
    

    results = list(filter(lambda x : len(x) > 1, dict1.values()))
    if(len(results))>0:
        f.write("Duplicates Found:\n")
        f.write("The following files are duplicate :")
        for result in results:
            for subresults in result:
                f.write("\t\t%s" % subresults)
                f.write('\n')
    
        f.close()
    else:
        f.write("No duplicates files are found")
        f.close()
     


def DeleteFiles(dict1):
    results = list(filter(lambda x : len(x)>1, dict1.values()))

    icnt = 0;
    if len(results) > 0:
        for result in results:
            for subresults in result:
                icnt += 1
                if icnt >= 2:
                    os.remove(subresults)
            icnt = 0
    else:
        print("No deuplicate files found .")


def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb') 
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def findDup(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isabs(path)
    dups = {}
    if exists:
        for dirName, dubdir, filenames in os.walk(path):
            print("Current Folder is :"+dirName)
            for file in filenames:
                path = os.path.join(dirName, file)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid Path")


def printResults(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values()))
    if(len(results))>0:
        print("Duplicates Found:")
        print("The following files are duplicate :")
        for result in results:
            for subresults in result:
                print("\t\t%s" % subresults)
    else:
        print("No duplicates files are found")

            

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
        starttime = time.time()
        arr ={}
        arr = findDup(argv[1])
        ProcessDisplay(arr)
        DeleteFiles(arr)
        endtime = time.time()
        print("Time required to perform the task is :" , endtime-starttime)


    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)
                                                        
if __name__ == "__main__":
    main()

