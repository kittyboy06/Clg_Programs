#include <stdio.h>
#define SIZE 7
int main() {
    int hash[SIZE] = {0};
    int keys[] = {10, 20, 5, 15};
    int n = 4, i, h, j;
    for(i = 0; i < n; i++) {
        h = keys[i] % SIZE;
        j = 1;
        while(hash[h] != 0) {
            h = (h + j*j) % SIZE; // quadratic probing
            j++;
        }
        hash[h] = keys[i];
    }
    printf("Hash table: ");
    for(i = 0; i < SIZE; i++)
        printf("%d ", hash[i]);
    return 0;
}
