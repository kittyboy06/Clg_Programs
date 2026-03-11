#include <stdio.h>

struct Hole {
    int size;
    int original_size;
};

struct process {
    int size;
    int allocated_hole; // Stores the index of the allocated hole
};

int main() {
    int nh, np;

    // 1. Input Number of Holes
    printf("Enter the Number of holes: ");
    scanf("%d", &nh);

    struct Hole holes[nh];

    for (int i = 0; i < nh; i++) {
        printf("Enter size of the hole %d: ", (i + 1));
        scanf("%d", &holes[i].size);
        holes[i].original_size = holes[i].size;
    }

    // 2. Input Number of Processes
    printf("\nEnter the Number of process: ");
    scanf("%d", &np);

    struct process processes[np];

    for (int i = 0; i < np; i++) {
        printf("Enter memory requirement of process %d: ", (i + 1));
        scanf("%d", &processes[i].size);
        processes[i].allocated_hole = -1; // -1 indicates unallocated
    }

    // 3. First Fit Allocation Logic
    for (int i = 0; i < np; i++) {
        for (int j = 0; j < nh; j++) {
            if (holes[j].size >= processes[i].size) {
                // Allocate process to this hole
                processes[i].allocated_hole = j;
                // Decrement available size in the hole
                holes[j].size -= processes[i].size;
                break; // Stop searching after the first fit is found
            }
        }
    }

    // 4. Print Process Allocation Status
    printf("\nProcess Allocation:\n");
    for (int i = 0; i < np; i++) {
        if (processes[i].allocated_hole != -1) {
            printf("Process %d is allocated to Hole %d\n", 
                    i + 1, processes[i].allocated_hole + 1);
        } else {
            printf("Process %d is unallocated\n", i + 1);
        }
    }

    // 5. Print Hole Status
    printf("\nHoles Status:\n");
    for (int i = 0; i < nh; i++) {
        printf("Hole %d: Original Size = %d, Remaining Size = %d\n", 
                i + 1, holes[i].original_size, holes[i].size);
    }

    return 0;
}