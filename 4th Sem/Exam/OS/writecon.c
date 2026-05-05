#include <stdio.h>

int main() {
    FILE *fp;
    char filename[50], content[200];

    printf("Enter file name: ");
    scanf("%s", filename);

    fp = fopen(filename, "w");

    printf("Enter content: ");
    getchar(); 
    fgets(content, sizeof(content), stdin);

    fprintf(fp, "%s", content);

    fclose(fp);

    printf("File created and written successfully\n");
    return 0;
}