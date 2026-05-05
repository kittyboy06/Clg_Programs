#include <stdio.h>
int main()
{
    int blocksize [20], processsize [20], allocation [20];
    int m, n;
    printf("Enter number of memory partitions: ");
    scanf("%d", &m);
    printf("Enter size of each block: \n");
    for (int i = 0; i < m; i++)
    {
        printf("Block %d: ", i);
        scanf("%d", &blocksize[i]);
    }
    printf("Enter number of processes: ");
    scanf("%d", &n);
    printf("Enter size of each process: \n");
    for (int i = 0; i < n; i++)
    {
        printf("Process %d: ", i);
        scanf("%d", &processsize[i]);
        allocation[i] = -1;
    }
    for (int i = 0; i < n; i++)
    {
        int bestfit = -1;
        for (int j = 0; j < m; j++)
        {
            if (blocksize[j] >= processsize[i])
            {
                if (bestfit == -1 || blocksize[bestfit] > blocksize[j])
                {
                    bestfit = j;
                }
            }
        }
        if (bestfit != -1)
        {
            allocation[i] = bestfit;
            blocksize[bestfit] -= processsize[i];
        }
    }
    printf("Process No.\tProcess Size\tPartition No.\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d\t\t%d\t\t", i, processsize[i]);
        if (allocation[i] != -1)
        {
            printf("%d\n", allocation[i]);
        }
        else
        {
            printf("Not Allocated\n");
        }
    }
    return 0;
}