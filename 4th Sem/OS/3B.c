#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

int main(int argc, char *argv[])
{
    int fd;
    char buf[1024];
    char line[200];
    int i = 0, n;

    if(argc < 3)
    {
        printf("Usage: ./a.out filename searchword\n");
        return 0;
    }

    // open file in read-only mode
    fd = open(argv[1], O_RDONLY);

    if(fd < 0)
    {
        printf("File does not exist\n");
        return 0;
    }

    // read file content
    while((n = read(fd, buf, sizeof(buf))) > 0)
    {
        for(int j = 0; j < n; j++)
        {
            if(buf[j] == '\n')
            {
                line[i] = '\0';

                if(strstr(line, argv[2]) != NULL)
                {
                    printf("%s\n", line);
                }

                i = 0;
            }
            else
            {
                line[i++] = buf[j];
            }
        }
    }

    close(fd);

    return 0;
}