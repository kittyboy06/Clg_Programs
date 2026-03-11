#include <stdio.h>

#define MAX_PROCESS 10
#define MAX_RESOURCE 10

int n, m;
int allocation[MAX_PROCESS][MAX_RESOURCE];
int max[MAX_PROCESS][MAX_RESOURCE];
int available[MAX_RESOURCE];
int need[MAX_PROCESS][MAX_RESOURCE];
int safesequence[MAX_PROCESS];

void calculateNeed()
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }
}

int isSafe()
{
    int work[MAX_RESOURCE];
    int finish[MAX_PROCESS] = {0};

    for(int i = 0; i < m; i++)
        work[i] = available[i];

    int count = 0;

    while(count < n)
    {
        int found = 0;

        for(int i = 0; i < n; i++)
        {
            if(!finish[i])
            {
                int j;
                for(j = 0; j < m; j++)
                {
                    if(need[i][j] > work[j])
                        break;
                }

                if(j == m)
                {
                    for(int k = 0; k < m; k++)
                        work[k] += allocation[i][k];

                    safesequence[count++] = i;
                    finish[i] = 1;
                    found = 1;
                }
            }
        }

        if(!found)
            return 0;
    }

    return 1;
}

int main()
{
    printf("Enter number of process: ");
    scanf("%d", &n);

    printf("Enter number of resources: ");
    scanf("%d", &m);

    printf("Enter the Allocation Matrix:\n");
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            scanf("%d", &allocation[i][j]);

    printf("Enter Max Matrix:\n");
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            scanf("%d", &max[i][j]);

    printf("Enter Available Resources:\n");
    for(int i = 0; i < m; i++)
        scanf("%d", &available[i]);

    calculateNeed();

    if(isSafe())
    {
        printf("System is in safe state\nSafe sequence: ");
        for(int i = 0; i < n; i++)
            printf("P%d ", safesequence[i]);
        printf("\n");
    }
    else
    {
        printf("System is in unsafe state\n");
    }

    return 0;
}