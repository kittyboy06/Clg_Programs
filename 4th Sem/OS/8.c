#include <stdio.h>

#define PAGE_SIZE 1024

int main()
{
    int process_size, virtual_address, total_pages;

    printf("Enter process size (bytes): ");
    scanf("%d", &process_size);

    /* Calculate number of pages required */
    total_pages = (process_size + PAGE_SIZE - 1) / PAGE_SIZE;

    int page_table[total_pages];

    printf("Enter frame mapping for %d pages\n", total_pages);

    for(int i = 0; i < total_pages; i++)
    {
        scanf("%d", &page_table[i]);
    }

    printf("Enter Virtual address : ");
    scanf("%d", &virtual_address);

    int page_number = virtual_address / PAGE_SIZE;
    int offset = virtual_address % PAGE_SIZE;

    if(page_number >= total_pages)
    {
        printf("Invalid virtual address\n");
        return 1;
    }

    int physical_address =
        (page_table[page_number] * PAGE_SIZE) + offset;

    printf("Physical Address : %d\n", physical_address);

    return 0;
}