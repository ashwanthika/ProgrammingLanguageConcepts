//Ashwanthika Umasankar
//UTA ID - 1001854976
//C version used - gcc (MinGW.org GCC-6.3.0-1) 6.3.0
//OS -  Windows

#include <stdio.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>

long directorySizeFunc(const char *folder, int flag) {
    long directorySize = 0;
    long baseDirectorySize=0;

    DIR *varDirectory; // setting a directory pointer
    struct dirent *dir_entry; // setting a struct named dir_entry
    struct stat fileStat; //setting a file stat struct

    if ((varDirectory = opendir(folder)) != NULL) //open the directory and read the contents 
    {
        while ((dir_entry = readdir(varDirectory)) != NULL) {
            char location[100];
            snprintf(location, sizeof(location), "%s/%s", folder, dir_entry->d_name); // Construct the full path and get the file status, check if it is a  file and add the filesize to  the totalsize else check if it is a directory and recursively calculate the total size of the subdirectories
            if (flag == 0) 
            {
                //calculate the filesize from base directory
                baseDirectorySize += (stat(location, &fileStat) == 0) ? (S_ISREG(fileStat.st_mode) ? fileStat.st_size : (S_ISDIR(fileStat.st_mode) && strcmp(dir_entry->d_name, ".") != 0 && strcmp(dir_entry->d_name, "..") != 0) ? 0 : 0) : 0;
            }
            //calculate directorr's total size
            directorySize += (stat(location, &fileStat) == 0) ? (S_ISREG(fileStat.st_mode) ? fileStat.st_size : (S_ISDIR(fileStat.st_mode) && strcmp(dir_entry->d_name, ".") != 0 && strcmp(dir_entry->d_name, "..") != 0) ? directorySizeFunc(location, flag + 1) : 0) : 0;
            }
            if(flag==0){
            printf("\nThe size of files present in the base directory: %ld\n", baseDirectorySize);}
            closedir(varDirectory);
    }

    return directorySize;
}

int main() {
    const char *currentDirectory = ".";
    long totalSize = directorySizeFunc(currentDirectory, 0);

    if (totalSize == 0) {
        printf("The directory is empty and the total size cannot be found\n");
    } else {
        printf("\nTotal size of the entire directory is: %ld bytes\n", totalSize);
    }

    return 0;
    
}
