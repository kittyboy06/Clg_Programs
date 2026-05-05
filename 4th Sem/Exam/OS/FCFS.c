#include <stdio.h>

int main() {
    int n;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    int bt[n], wt[n], tat[n];

    printf("Enter burst times:\n");
    for (int i = 0; i < n; i++)
        scanf("%d", &bt[i]);

    // Waiting Time
    wt[0] = 0;
    for (int i = 1; i < n; i++)
        wt[i] = wt[i-1] + bt[i-1];

    // Turnaround Time
    for (int i = 0; i < n; i++)
        tat[i] = wt[i] + bt[i];

    // Table Output
    printf("\nProcess\tBT\tWT\tTAT\n");
    for (int i = 0; i < n; i++)
        printf("P%d\t%d\t%d\t%d\n", i+1, bt[i], wt[i], tat[i]);

    // Gantt Chart
    printf("\nGantt Chart:\n|");
    for (int i = 0; i < n; i++)
        printf("  P%d  |", i+1);

    printf("\n0");
    int time = 0;
    for (int i = 0; i < n; i++) {
        time += bt[i];
        printf("     %d", time);
    }

    printf("\n");

    return 0;
}