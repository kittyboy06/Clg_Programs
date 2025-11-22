#include <stdio.h>
#define SIZE 7
int main() {
    int hash[SIZE] = {0}, key, i, h;
    int keys[] = {10, 20, 5, 15};
    int n = 4;
    for(i = 0; i < n; i++) {
        key = keys[i];
        h = key % SIZE;
        while(hash[h] != 0)
            h = (h + 1) % SIZE;
        hash[h] = key;
    }
printf("Hash table: ");
    for(i = 0; i < SIZE; i++)
        printf("%d ", hash[i]);
    return 0;
}
