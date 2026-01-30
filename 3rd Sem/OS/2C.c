#include<stdio.h>
#include<stdlib.h>
#include<sys/stat.h>
#include<time.h>
int main(int argsc, char *argv[])
{
    struct stat file;
    int n;
    if(argsc != 2)
    {
        printf("Usage: ./a.out <filename>\n");
        exit(1);
    }
    if((n = stat(argv[1], &file)) == -1)
    {
        perror(argv[1]);
        exit(1);
    }
    printf("User ID: %d\n", file.st_uid);
    printf("Group ID: %ld\n", (long)file.st_gid);
    printf("Block size: %ld\n", (long)file.st_blksize);
    printf("Blocks allocated: %ld\n", (long)file.st_blocks);
    printf("Node number: %ld\n", (long)file.st_ino);
    printf("Last accessed: %s", ctime(&file.st_atime));
    printf("Last modified: %s", ctime(&file.st_mtime));
    printf("File size: %ld bytes\n", (long)file.st_size);
    printf("Number of links: %ld\n", (long)file.st_nlink);
    printf("Permissions");
    printf( (S_ISDIR(file.st_mode)) ? " d" : "-");
    printf((file.st_mode & S_IRUSR) ? "r" : "-");
    printf((file.st_mode & S_IWUSR) ? "w" : "-");
    printf((file.st_mode & S_IXUSR) ? "x" : "-");
    printf((file.st_mode & S_IRGRP) ? "r" : "-");
    printf((file.st_mode & S_IWGRP) ? "w" : "-");
    printf((file.st_mode & S_IXGRP) ? "x" : "-");
    printf((file.st_mode & S_IROTH) ? "r" : "-");
    printf((file.st_mode & S_IWOTH) ? "w" : "-");
    printf((file.st_mode & S_IXOTH) ? "x" : "-");

    if(S_ISREG(file.st_mode))
    {
        printf("\nIt is a regular file.\n");
    }
    if(S_ISDIR(file.st_mode))
    {
        printf("\nIt is a directory.\n");
    }
    return 0;
}