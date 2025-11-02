#include <stdio.h>
int main() {
    int arr[] = {5, 2, 8, 1, 3};
    int n = 5, i, j, min, temp;
    for(i=0; i<n-1; i++){
        min = i;
        for(j=i+1; j<n; j++)
            if(arr[j] < arr[min]) min = j;
        if(min != i){
            temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }

    printf("Sorted array: ");
    for(i=0;i<n;i++) printf("%d ",arr[i]);
    printf("\n");
    return 0;
}
