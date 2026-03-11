#include <stdio.h>
#include <dirent.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char path[1000];
    struct dirent **files;
    int n, i;

    // Get current working directory
    getcwd(path, sizeof(path));

    // Scan directory and sort entries
    n = scandir(path, &files, NULL, alphasort);

    if (n < 0)
    {
        perror("scandir");
        exit(1);
    }

    printf("Files in current directory:\n");

    // Display file names except hidden files
    for(i = 0; i < n; i++)
    {
        if(files[i]->d_name[0] != '.')
        {
            printf("%s\n", files[i]->d_name);
        }
        free(files[i]);
    }

    free(files);

    return 0;
}
