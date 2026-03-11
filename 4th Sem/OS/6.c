#include <stdio.h>
#include <stdbool.h>

#define MAX 10

int main()
{
    int p, r;
    int alloc[MAX][MAX], req[MAX][MAX];
    int avail[MAX];
    int work[MAX];
    bool finish[MAX];
    bool marked[MAX];

    printf("Enter number of processes: ");
    scanf("%d", &p);

    printf("Enter number of resources: ");
    scanf("%d", &r);

    printf("\nEnter Allocation Matrix:\n");
    for(int i = 0; i < p; i++)
    {
        for(int j = 0; j < r; j++)
        {
            scanf("%d", &alloc[i][j]);
        }
    }

    printf("\nEnter Request Matrix:\n");
    for(int i = 0; i < p; i++)
    {
        for(int j = 0; j < r; j++)
        {
            scanf("%d", &req[i][j]);
        }
    }

    printf("\nEnter Available Resources:\n");
    for(int i = 0; i < r; i++)
    {
        scanf("%d", &avail[i]);
        work[i] = avail[i];
    }

    for(int i = 0; i < p; i++)
    {
        marked[i] = false;
    }

    int progress;

    do
    {
        progress = 0;

        for(int i = 0; i < p; i++)
        {
            if(!marked[i])
            {
                bool possible = true;

                for(int j = 0; j < r; j++)
                {
                    if(req[i][j] > work[j])
                    {
                        possible = false;
                        break;
                    }
                }

                if(possible)
                {
                    marked[i] = true;

                    for(int j = 0; j < r; j++)
                    {
                        work[j] = work[j] + alloc[i][j];
                    }

                    progress = 1;
                }
            }
        }

    } while(progress);

    int deadlock = 0;

    for(int i = 0; i < p; i++)
    {
        if(!marked[i])
        {
            printf("Deadlock detected at P%d\n", i);
            deadlock = 1;
        }
    }

    if(!deadlock)
        printf("No deadlock detected\n");

    return 0;
}