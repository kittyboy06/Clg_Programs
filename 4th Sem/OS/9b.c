#include <stdio.h>

// Function to find the index of the Least Recently Used page
int findLRU(int time[], int n) {
    int i, minimum = time[0], pos = 0;
    for (i = 1; i < n; ++i) {
        if (time[i] < minimum) {
            minimum = time[i];
            pos = i;
        }
    }
    return pos;
}

int main() {
    int rs[100], frame[10], time[10];
    int i, j, pos, fault = 0, count = 0, nf, len, flag1, flag2;

    printf("Enter length of the reference string: ");
    scanf("%d", &len);

    printf("Enter the reference string: ");
    for (i = 0; i < len; i++) {
        scanf("%d", &rs[i]);
    }

    printf("Enter number of frames: ");
    scanf("%d", &nf);

    // Initialize frames with -1 (empty)
    for (i = 0; i < nf; ++i) {
        frame[i] = -1;
    }

    for (i = 0; i < len; ++i) {
        flag1 = flag2 = 0;

        // Check if page already exists in a frame (Page Hit)
        for (j = 0; j < nf; ++j) {
            if (frame[j] == rs[i]) {
                count++;
                time[j] = count; // Update the "time" counter for LRU
                flag1 = flag2 = 1;
                break;
            }
        }

        // If page is not in frame and there is empty space
        if (flag1 == 0) {
            for (j = 0; j < nf; ++j) {
                if (frame[j] == -1) {
                    count++;
                    fault++;
                    frame[j] = rs[i];
                    time[j] = count;
                    flag2 = 1;
                    break;
                }
            }
        }

        // If page is not in frame and frames are full (Page Replacement)
        if (flag2 == 0) {
            pos = findLRU(time, nf);
            count++;
            fault++;
            frame[pos] = rs[i];
            time[pos] = count;
        }

        // Display current frame state
        printf("Page %d: ", rs[i]);
        for (j = 0; j < nf; ++j) {
            if (frame[j] != -1)
                printf("%d ", frame[j]);
            else
                printf("- ");
        }
        printf("\n");
    }

    printf("\nTotal Page Faults = %d\n", fault);

    return 0;
}