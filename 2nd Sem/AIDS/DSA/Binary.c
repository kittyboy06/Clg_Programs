#include <stdio.h>
int main() {
    int arr[] = {1, 3, 5, 7, 9}, n = 5, key = 5;
    int low = 0, high = n - 1, mid;
     while(low <= high) {
        mid = (low + high) / 2;
        if(arr[mid] == key) {
            printf("Element %d found at index %d\n", key, mid);
            return 0;
        } else if(arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
 printf("Element %d not found\n", key);
    return 0;
}
