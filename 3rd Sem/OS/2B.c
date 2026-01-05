#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>

int main()
{
    int i, status;
    pid_t pid;
    if(pid < 0)
    {
        printf("Fork failed\n");
        exit(1);
    }
    else if(pid > 0)
    {
        wait(NULL);
        printf("\nparent Starts\n Even numbers:");
        for(i = 2; i <= 10; i += 2)
        {
            printf(" %d ", i);
        }
        printf("\nparent Ends\n");
        
    }
    else if(pid == 0)
    {
        printf("child Starts\n Odd numbers:");
        for(i = 1; i < 10; i += 2)
        {
            printf(" %d ", i);
        }
        printf("\nchild Ends\n");
    }
    return 0;
}