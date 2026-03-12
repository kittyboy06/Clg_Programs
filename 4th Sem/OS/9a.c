#include <stdio.h>

void fifo_page_replacement(int reference_string[], int n, int f)
{
    int frames[f];
    int i, j, k;
    int page_faults = 0;
    int index = 0;
    int found;

    for(i = 0; i < f; i++)
        frames[i] = -1;

    for(i = 0; i < n; i++)
    {
        found = 0;

        for(j = 0; j < f; j++)
        {
            if(frames[j] == reference_string[i])
            {
                found = 1;
                break;
            }
        }

        if(!found)
        {
            frames[index] = reference_string[i];
            index = (index + 1) % f;
            page_faults++;

            printf("Page %d caused a page fault. Frame state: [", reference_string[i]);

            for(k = 0; k < f; k++)
                printf("%d ", frames[k]);

            printf("]\n");
        }
        else
        {
            printf("Page %d is already in the frame. Frame state: [", reference_string[i]);

            for(k = 0; k < f; k++)
                printf("%d ", frames[k]);

            printf("]\n");
        }
    }

    printf("\nTotal page faults: %d\n", page_faults);
}

int main()
{
    int reference_string[] = {7,0,1,2,0,3,0,4,2,3,0,3,2};
    int n = sizeof(reference_string) / sizeof(reference_string[0]);
    int frames = 3;

    fifo_page_replacement(reference_string, n, frames);

    return 0;
}