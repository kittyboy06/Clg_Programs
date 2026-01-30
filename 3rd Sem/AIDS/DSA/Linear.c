#include <stdio.h>
int main() {
    int arr[] = {5, 3, 7, 1, 9};
    int n = 5, key = 7, i, found = 0;
     for(i = 0; i < n; i++) {
        if(arr[i] == key) {
            found = 1;
            break;
        }
    }
         if(found)
        printf("Element %d found at index %d\n", key, i);
    else
        printf("Element %d not found\n", key);
        return 0;
}
