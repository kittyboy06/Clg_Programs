#include<stdio.h>
#include<conio.h>

int main()
{
    int mat[5][5], i, j, temp;
    printf("Enter elements of 5x5 matrix:\n");
    for(i = 0; i < 5; i++)
    {
        for(j = 0; j < 5; j++)
        {
            printf("Element [%d][%d]: ", i, j);
            scanf("%d", &mat[i][j]);
        }
    }
    
    temp = mat[0][0];
    mat[0][0] = mat[4][4];
    mat[4][4] = temp;
    printf("\nMatrix after swapping [0][0] and [4][4]:\n");
    for(i = 0; i < 5; i++)
    {
        for(j = 0; j < 5; j++)
        {
            printf("%d\t", mat[i][j]);
        }
        printf("\n");
    }
}