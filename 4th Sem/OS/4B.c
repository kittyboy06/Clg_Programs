#include <stdio.h>

struct process
{
    int pid;
    int btime;
    int wtime;
    int ttime;
};

void sort_process(struct process p[], int n)
{
    struct process temp;

    for(int i=0;i<n-1;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(p[i].btime > p[j].btime)
            {
                temp = p[i];
                p[i] = p[j];
                p[j] = temp;
            }
        }
    }
}

void calculate_time(struct process p[], int n)
{
    p[0].wtime = 0;
    p[0].ttime = p[0].btime;

    for(int i=1;i<n;i++)
    {
        p[i].wtime = p[i-1].wtime + p[i-1].btime;
        p[i].ttime = p[i].wtime + p[i].btime;
    }
}

void display_gantt(struct process p[], int n)
{
    printf("\nGantt Chart\n");

    for(int i=0;i<n;i++)
        printf("----");
    printf("\n|");

    for(int i=0;i<n;i++)
        printf("P%d |",p[i].pid);

    printf("\n");

    for(int i=0;i<n;i++)
        printf("----");

    printf("\n0");

    for(int i=0;i<n;i++)
        printf("   %d",p[i].ttime);

    printf("\n");
}

int main()
{
    int n;
    float awt=0, atat=0;

    printf("Enter number of processes: ");
    scanf("%d",&n);

    struct process p[n];

    for(int i=0;i<n;i++)
    {
        p[i].pid = i+1;
        printf("Enter burst time for P%d: ",p[i].pid);
        scanf("%d",&p[i].btime);
    }

    sort_process(p,n);
    calculate_time(p,n);

    printf("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time\n");

    for(int i=0;i<n;i++)
    {
        printf("P%d\t%d\t\t%d\t\t%d\n",
        p[i].pid,p[i].btime,p[i].wtime,p[i].ttime);

        awt += p[i].wtime;
        atat += p[i].ttime;
    }

    awt /= n;
    atat /= n;

    display_gantt(p,n);

    printf("\nAverage Waiting Time = %.2f",awt);
    printf("\nAverage Turnaround Time = %.2f\n",atat);

    return 0;
}
