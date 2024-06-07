import os

def main():
    print("Enter the name of the file :")
    file = input()


    if os.path.exists(file):
        print("File is present")

        content = open(file,"r")
        for line in content:
            print(line.strip("\n"))
        content.close()


    else:
        print("File not present")


if __name__ == "__main__":
    main()