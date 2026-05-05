#include <stdio.h>

int main() {
    int n;

    printf("Enter number of pages: ");
    scanf("%d", &n);

    int pageTable[n];

    printf("Enter frame numbers:\n");
    for (int i = 0; i < n; i++)
        scanf("%d", &pageTable[i]);

    int page, offset;

    printf("Enter page number: ");
    scanf("%d", &page);

    printf("Enter offset: ");
    scanf("%d", &offset);

    int physical = pageTable[page] * 100 + offset;

    printf("Physical Address = %d\n", physical);

    return 0;
}