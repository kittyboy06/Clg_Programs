#include <stdio.h>

int main() {
    FILE *src, *dest;
    char srcName[50], destName[50], ch;

    printf("Enter source file: ");
    scanf("%s", srcName);

    printf("Enter destination file: ");
    scanf("%s", destName);

    src = fopen(srcName, "r");
    if (src == NULL) {
        printf("Source file not found\n");
        return 1;
    }

    dest = fopen(destName, "w");

    while ((ch = fgetc(src)) != EOF)
        fputc(ch, dest);

    printf("File copied successfully\n");

    fclose(src);
    fclose(dest);
    return 0;
}