#include <stdio.h>

int main() {
    int m, n;

    printf("Enter number of blocks: ");
    scanf("%d", &m);
    int blockSize[m];

    printf("Enter block sizes:\n");
    for (int i = 0; i < m; i++)
        scanf("%d", &blockSize[i]);

    printf("Enter number of processes: ");
    scanf("%d", &n);
    int processSize[n], allocation[n];

    printf("Enter process sizes:\n");
    for (int i = 0; i < n; i++)
        scanf("%d", &processSize[i]);

    for (int i = 0; i < n; i++)
    {
        int worst = -1;
        for (int j = 0; j < m; j++) 
        {
            if (blockSize[j] >= processSize[i]) 
            {
                if (worst == -1 || blockSize[j] > blockSize[worst])
                    worst = j;
            }
        }

        if (worst != -1) 
        {
            allocation[i] = worst;
            blockSize[worst] -= processSize[i];
        } 
        else 
        {
            allocation[i] = -1;
        }
    }

    for (int i = 0; i < n; i++)
    {
        printf("Process %d -> Block %d\n", i+1, allocation[i]+1);
    }

    return 0;
}