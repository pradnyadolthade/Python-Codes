import os

def main():
    print("Enter the name of the file :")
    file = input()


    if os.path.exists(file):
        print("File is present")
    else:
        print("File not present")


if __name__ == "__main__":
    main()