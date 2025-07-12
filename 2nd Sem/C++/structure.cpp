#include <iostream>
using namespace std;

struct demo
{
    char name[20];
    int roll;
    int marks;
    int phno;
}a[100];

int main()
{
    int n;
    cout << "Enter the number of students: ";
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cout << "Enter name, roll number, marks, and phone number for student " << i + 1 << ": ";
        cin >> a[i].name >> a[i].roll >> a[i].marks >> a[i].phno;
    }

    cout << "\nStudent Details:\n";
    for (int i = 0; i < n; i++)
    {
        cout << "Name: " << a[i].name 
             << ", Roll No: " << a[i].roll 
             << ", Marks: " << a[i].marks 
             << ", Phone No: " << a[i].phno << endl;
    }

    return 0;
}