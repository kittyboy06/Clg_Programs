#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    int fd1, fd2, n;
    char buf[1024];

    if(argc < 3)
    {
        printf("Provide source and destination file\n");
        return 0;
    }

    fd1 = open(argv[1], O_RDONLY);

    if(fd1 < 0)
    {
        printf("Source file does not exist\n");
        return 0;
    }

    fd2 = creat(argv[2], 0644);

    if(fd2 < 0)
    {
        printf("Cannot create destination file\n");
        return 0;
    }

    while((n = read(fd1, buf, 1024)) > 0)
    {
        write(fd2, buf, n);
    }

    close(fd1);
    close(fd2);

    printf("File copied successfully\n");

    return 0;
}
