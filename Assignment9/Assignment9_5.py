import os

def main():
    print("Enter the name of the first file:")
    file1 = input()
    print("Enter string that you want to check frequency:")
    str1 = input()

    if os.path.exists(file1):
        print("File is present")

        content1 = open(file1, "r")    
        count = 0
        for line in content1:
            words = line.split()
            for word in words:
                if word == str1:
                    count += 1 
        
        print("Frequnecy is ",count)
    else:
        print("Files not present")

if __name__ == "__main__":
    main()
