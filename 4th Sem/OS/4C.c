#include <stdio.h>

void roundRobin(int processes[], int n, int burst_time[], int quantum)
{
    int remaining_bt[n], wait_time[n], turnaround_time[n];

    for (int i = 0; i < n; i++)
        remaining_bt[i] = burst_time[i];

    int t = 0;

    printf("\nProcess Execution Order:\n");

    while (1)
    {
        int done = 1;

        for (int i = 0; i < n; i++)
        {
            if (remaining_bt[i] > 0)
            {
                done = 0;

                if (remaining_bt[i] > quantum)
                {
                    t += quantum;
                    remaining_bt[i] -= quantum;

                    printf("Process %d executed for %d units (Time: %d)\n",
                           processes[i], quantum, t);
                }
                else
                {
                    t += remaining_bt[i];

                    printf("Process %d executed for %d units (Completed at Time: %d)\n",
                           processes[i], remaining_bt[i], t);

                    turnaround_time[i] = t;
                    wait_time[i] = turnaround_time[i] - burst_time[i];
                    remaining_bt[i] = 0;
                }
            }
        }

        if (done == 1)
            break;
    }

    printf("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time\n");

    for (int i = 0; i < n; i++)
    {
        printf("%d\t%d\t\t%d\t\t%d\n",
               processes[i], burst_time[i], wait_time[i], turnaround_time[i]);
    }
}

int main()
{
    int n, quantum;

    printf("Enter Number of processes: ");
    scanf("%d", &n);

    int processes[n], burst_time[n];

    for (int i = 0; i < n; i++)
    {
        processes[i] = i + 1;
        printf("Enter burst time for process %d: ", i + 1);
        scanf("%d", &burst_time[i]);
    }

    printf("Enter time quantum: ");
    scanf("%d", &quantum);

    roundRobin(processes, n, burst_time, quantum);

    return 0;
}