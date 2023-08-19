# Ashwanthika Umasankar
#UTA ID - 1001854976
#Python version used - Python 3.9.13
#OS -  Windows

import os #import the OS module

#Function that computes the total size of its dorectory an its contents while taking in a parameter 
def directorySize(folder,flag):
    #Setting the initial size to be returned at a later point as 0
    dirSize = 0 
    baseDirSize=0
    if flag==0:
        for var in os.scandir(folder):
            if var.is_file():
                baseDirSize += var.stat().st_size 
        print("\nThe size of files present in base directory:",baseDirSize )
    for var in os.scandir(folder):
        if var.is_file():
            dirSize += var.stat().st_size # Add the size of the file to the size
        elif var.is_dir():
            subdir_size = directorySize(var.path, flag+1) # Recursively calculate the size of the subdirectory
            #print(f"\n Size of subdirectory located at the path {var.path}: {subdir_size} bytes\n") # Print the size of the subdirectory along with its path
            dirSize += subdir_size # Add the size of the subdirectory to the  size

    return dirSize
#get the current directory
def currentDirectory():
    return os.path.dirname(os.path.abspath(__file__))

def main():
    current_directory = currentDirectory()
    total_size = directorySize(current_directory,0) #get the current directory and pass it to the function and compute the total size of directory and subdirectories

    if total_size == 0:
        print("The directory is empty and the total size cannot be found")
    else:
        print(f"\nTotal size of the entire directory is: {total_size} bytes\n")

if __name__ == "__main__":
    main()

