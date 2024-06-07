import os 
import sys


def Directorytraversal(DirName, Extention1,Extention2):
    flag = os.path.isdir(DirName)

    if(flag == False):
        DirName = os.path.abspath(DirName)

    exists = os.path.isdir(DirName)
    if(exists == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                if name.endswith(Extention1):
                    new_name = name.replace(Extention1,Extention2)
                    os.rename(os.path.join(foldername,name),os.path.join(foldername,new_name))
                    print(new_name)




def main():
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to perform Directory traversal")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of the script : ")
            print("Name_Of_File  Name_Of_Directory  Extentipon_Of_File")
            exit()
    
    if(len(sys.argv)==4):
        try:
            Directorytraversal(sys.argv[1],sys.argv[2],sys.argv[3])

        except Exception as eobj:
            print("Unable to perform task due to :",eobj)
    else:
        print("Invalid option")
        print("Use --h option to get the help and use --u option to get the usage of application")
        exit()

if __name__ == "__main__":
    main()