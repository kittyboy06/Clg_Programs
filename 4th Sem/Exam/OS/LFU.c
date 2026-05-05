#include <stdio.h>

int main() {
    int n, f;

    printf("Enter number of pages: ");
    scanf("%d", &n);
    int pages[n];

    printf("Enter page reference string:\n");
    for (int i = 0; i < n; i++)
        scanf("%d", &pages[i]);

    printf("Enter number of frames: ");
    scanf("%d", &f);

    int frames[f], freq[100] = {0}, faults = 0;

    for (int i = 0; i < f; i++)
        frames[i] = -1;

    for (int i = 0; i < n; i++) {
        freq[pages[i]]++;

        int found = 0;
        for (int j = 0; j < f; j++) {
            if (frames[j] == pages[i]) {
                found = 1;
                break;
            }
        }

        if (!found) {
            int lfu = 0;
            for (int j = 1; j < f; j++)
                if (freq[frames[j]] < freq[frames[lfu]])
                    lfu = j;

            frames[lfu] = pages[i];
            faults++;
        }
    }

    printf("Page Faults = %d\n", faults);
    return 0;
}