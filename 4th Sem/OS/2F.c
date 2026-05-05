#include <stdio.h>
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
