//Ashwanthika Umasankar
//UTA ID - 1001854976
//java version "19.0.2"
//OS -  Windows



import java.io.File;

public class axu4976_lab01 {
    //function directorysize used to compute the total size of a directory and its contents
    //function takes a file object input and returns a long value representing the totalsize using recursion 
    private static long directorySize(File folder,  int flag) {
        long directorySize = 0;
        long baseDirSize = 0;
        //set flag as 0 and compute the size of files belonging oto base dir
        if (flag == 0) {
        File[] fileArray = folder.listFiles();
            if (fileArray != null) {
                int count = fileArray.length;
                int var = 0;
                while (var < count) {
                    File file = fileArray[var];
                    if (file.isFile()) {
                        baseDirSize += file.length();
                    }
                    var++;
                }
            }
        System.out.println("\nThe size of files present in the base directory: " + baseDirSize);
        }
        //add the size and recursively comute subdirectory size
        File[] fileArray  = folder.listFiles();
        if (fileArray != null) {
            int count = fileArray.length;
            int var = 0;
            while (var < count) {
                File file = fileArray[var];
                if (file.isFile()) {
                    directorySize += file.length();
                } else if (file.isDirectory()) {
                    directorySize += directorySize(file, flag+1);
                }
                var++;
            }
        }

        return directorySize;
    }

    public static void main(String[] args) {
        File currentDirectory = new File("."); 
        long totalSize = directorySize(currentDirectory, 0); //get the current directory and pass it to the function and compute the total size of directory and subdirectories

        if (totalSize == 0) {
            System.out.println("The directory is empty and the total size cannot be found");
        } else {
            System.out.println("Total size of the entire directory is " + totalSize + " bytes");
        }
    }
}