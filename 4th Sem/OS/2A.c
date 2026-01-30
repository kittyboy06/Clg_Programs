#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>

int main()
{
    pid_t pid;
    int x = 5;
    pid = fork();
    if(pid < 0)
    {
        printf("Fork failed\n");
        exit(1);
    }
    else if(pid == 0)
    {
        printf("child process:\n");
        printf("In process id: %d\n", getpid());
        printf("Value of x : %d\n", x);
        printf("In parent id: %d\n", getppid());
    }
    else
    {
        printf("parent process:\n");
        printf("In process id: %d\n", getpid());
        printf("Value of x : %d\n", x);
        printf("In process if shell: %d\n", getppid());
    }
    return 0;
}