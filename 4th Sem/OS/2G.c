#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int fd;
    char buf[100];
    int n;

    // check if filename is given
    if(argc < 2)
    {
        printf("Please provide file name\n");
        return 1;
    }

    // open file in append mode
    fd = open(argv[1], O_APPEND | O_WRONLY | O_CREAT, 0644);

    if(fd < 0)
    {
        printf("Error opening file\n");
        return 1;
    }

    printf("Enter text (Press Ctrl+D to stop):\n");

    // read from keyboard and write to file
    while((n = read(0, buf, 100)) > 0)
    {
        write(fd, buf, n);
    }

    // close file
    close(fd);

    printf("Data appended successfully.\n");

    return 0;
}