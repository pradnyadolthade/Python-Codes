import os 
import sys

def copy_file(source_file, destination_file):
    try:
        file1 = open(source_file,'rb')
        file2 = open(destination_file,'wb')
        file2.write(file1.read())
        print(f"File {source_file} copied to {destination_file}")
        file1.close()
        file2.close()

    except IOError as e:
        print(f"Unable to copy file '{source_file}' to '{destination_file}': {e.strerror}")



def Directorytraversal(DirName1,DirName2):
    flag1 = os.path.isdir(DirName1)
    
    if not os.path.isdir(DirName2):
        os.mkdir(DirName2)
        print(f"Directory '{DirName2}' created successfully.")
    else:
        print("directory already exists.")
    if(flag1 == False):
        DirName1 = os.path.abspath(DirName1)

    exists = os.path.isdir(DirName1)
    if(exists == True):
        for foldername, subfoldername, filename in os.walk(DirName1):
            for name in filename:
                source_file_path = os.path.join(foldername, name)
                destination_file_path = os.path.join(DirName2, name)
                copy_file(source_file_path, destination_file_path)
                



def main():
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to perform Directory traversal")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of the script : ")
            print("Name_Of_File  Name_Of_Directory  Extentipon_Of_File")
            exit()
    
    if(len(sys.argv)==3):
        try:
            Directorytraversal(sys.argv[1],sys.argv[2])

        except Exception as eobj:
            print("Unable to perform task due to :",eobj)
    else:
        print("Invalid option")
        print("Use --h option to get the help and use --u option to get the usage of application")
        exit()

if __name__ == "__main__":
    main()