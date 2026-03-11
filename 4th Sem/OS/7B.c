#include <stdio.h>
#include <stdlib.h>

// Function to sort holes in descending order for Worst Fit
void sortdescending(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] < arr[j + 1]) { // Descending check
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void worstFitAllocation(int holes[], int numholes, int processes[], int numprocesses) {
    int *sortedHoles = (int *)malloc(numholes * sizeof(int));
    int *originalHoles = (int *)malloc(numholes * sizeof(int));
    int *allocation = (int *)malloc(numprocesses * sizeof(int));

    for (int i = 0; i < numholes; i++) {
        originalHoles[i] = holes[i];
        sortedHoles[i] = holes[i];
    }

    // Initialize allocation with -1 (not allocated)
    for (int i = 0; i < numprocesses; i++) {
        allocation[i] = -1;
    }

    // Allocation logic
    for (int i = 0; i < numprocesses; i++) {
        // Sort holes every time to find the current largest available hole
        sortdescending(sortedHoles, numholes);
        
        if (sortedHoles[0] >= processes[i]) {
            // Find which original hole this corresponds to
            for (int j = 0; j < numholes; j++) {
                if (holes[j] == sortedHoles[0]) {
                    allocation[i] = j;
                    holes[j] -= processes[i];
                    sortedHoles[0] -= processes[i]; // Update the sorted copy
                    break;
                }
            }
        }
    }

    // Print Process Allocation
    printf("\nProcess Allocation:\n");
    for (int i = 0; i < numprocesses; i++) {
        if (allocation[i] != -1) {
            printf("Process %d allocated to Hole %d\n", i + 1, allocation[i] + 1);
        } else {
            printf("Process %d could not be allocated\n", i + 1);
        }
    }

    // Print Final Hole Status
    printf("\nFinal Hole Status:\n");
    for (int i = 0; i < numholes; i++) {
        printf("Hole %d: Original Size = %d, Remaining Size = %d\n", 
               i + 1, originalHoles[i], holes[i]);
    }

    free(sortedHoles);
    free(originalHoles);
    free(allocation);
}

int main() {
    int holes[] = {100, 500, 200, 300, 600};
    int numholes = sizeof(holes) / sizeof(holes[0]);
    
    int processes[] = {212, 417, 112, 426};
    int numprocesses = sizeof(processes) / sizeof(processes[0]);

    worstFitAllocation(holes, numholes, processes, numprocesses);

    return 0;
}