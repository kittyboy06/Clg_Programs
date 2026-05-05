/*#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    int fd, n;
    char buf[100];

    if (argc != 2)
    {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    fd = open(argv[1], O_RDONLY);

    if (fd < 0)
    {
        printf("File does not exist\n");
        return 1;
    }

    printf("File contents:\n");

    while ((n = read(fd, buf, 100)) > 0)
    {
        write(1, buf, n);
    }

    close(fd);

    return 0;
}
*/
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    char *filename = argv[1];

    int fd = open(filename, O_RDONLY);
    if (fd == -1)
    {
        perror("ERROR OPENING FILE");
        exit(EXIT_FAILURE);
    }

    char buf[100];
    ssize_t bytesRead;

    while ((bytesRead = read(fd, buf, sizeof(buf))) > 0)
    {
        write(STDOUT_FILENO, buf, bytesRead);
    }

    if (bytesRead == -1)
    {
        perror("ERROR reading file");
        close(fd);
        exit(EXIT_FAILURE);
    }