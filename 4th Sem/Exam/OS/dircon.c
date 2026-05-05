#include <stdio.h>
#include <dirent.h>

int main() {
    char path[100];
    struct dirent *entry;
    DIR *dir;

    printf("Enter directory path: ");
    scanf("%s", path);

    dir = opendir(path);

    if (dir == NULL) {
        printf("Cannot open directory\n");
        return 1;
    }

    while ((entry = readdir(dir)) != NULL)
        printf("%s\n", entry->d_name);
    printf("\n");
    closedir(dir);
    return 0;
}