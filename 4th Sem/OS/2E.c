    #include <stdio.h>
    #include <stdlib.h>
    #include <fcntl.h>
    #include <unistd.h>
    #include <string.h>

    int main(int argc, char *argv[])
    {
        int fd, n;
        char buf[100];

        if (argc != 2)
        {
            printf("Usage: %s <filename>\n", argv[0]);
            return 1;
        }

        fd = open(argv[1], O_CREAT | O_TRUNC | O_WRONLY, 0644);

        if (fd < 0)
        {
            perror("Error creating file");
            return 1;
        }

        printf("File is created successfully. You can start typing:\n");
        printf("Type Ctrl+D to stop input.\n");

        n = read(STDIN_FILENO, buf, sizeof(buf));

        if (n < 0)
        {
            perror("Error reading input");
            return 1;
        }
        