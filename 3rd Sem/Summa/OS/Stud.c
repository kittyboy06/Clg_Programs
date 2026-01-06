#include <stdio.h>
#include <conio.h>

int main() {
    int roll_no;
    char name[50];
    float marks;

    printf("Enter Roll Number: ");
    scanf("%d", &roll_no);
    printf("Enter Name: ");
    scanf("%s", name);
    printf("Enter Marks: ");
    scanf("%f", &marks);

    printf("\nStudent Details:\n");
    printf("Roll Number: %d\n", roll_no);
    printf("Name: %s\n", name);
    printf("Marks: %.2f\n", marks);

    getch();
    return 0;
}