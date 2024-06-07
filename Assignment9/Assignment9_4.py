import os

def main():
    print("Enter the name of the first file:")
    file1 = input()
    print("Enter the name of the second file:")
    file2 = input()

    if os.path.exists(file1) and os.path.exists(file2):
        print("Files are present")

        content1 = open(file1, "r")   
        content2 = open(file2, "r")  
        flag = True
        for line1, line2 in zip(content1, content2):
            if line1 != line2:
                flag = False
                break

        if flag:
            print("Success: Files have the same content.")
        else:
            print("Failed: Files have different content.")

    else:
        print("Files not present")

if __name__ == "__main__":
    main()
