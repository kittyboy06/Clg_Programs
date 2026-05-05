#include <stdio.h>
#include <dirent.h>

int main(int argc, char *argv[])
{
    DIR *dir;
    struct dirent *entry;

    // Check if directory name is provided
    if (argc != 2)
    {
        printf("Usage: %s <directory_name>\n", argv[0]);
        return 1;
    }

    // Open directory
    dir = opendir(argv[1]);

    if (dir == NULL)
    {
        printf("Error: Cannot open directory\n");
        return 1;
    }

    // Read and display directory contents
    printf("Contents of directory '%s':\n", argv[1]);

    while ((entry = readdir(dir)) != NULL)
    {
        printf("%s\n", entry->d_name);
    }

    // Close directory
    closedir(dir);

    return 0;
}