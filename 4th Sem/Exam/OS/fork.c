#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        printf("Fork failed\n");
    } else if (pid == 0) {
        printf("Child Process\nPID = %d\n", getpid());
    } else {
        printf("Parent Process\nPID = %d\nChild PID = %d\n", getpid(), pid);
    }

    return 0;
}