#include <iostream>
using namespace std;

class Student {
    char name[20];
    int roll;
    int marks;
    int phno;
    
    void displayData() {
        cout << "Name: " << name
             << ", Roll No: " << roll
             << ", Marks: " << marks
             << ", Phone No: " << phno << endl;
    }

public:
    void getData() {
        cout << "Enter name, roll number, marks, and phone number: ";
        cin >> name >> roll >> marks >> phno;
    }

    void display()
    {
        displayData();
    }

};

int main() {
    Student a[100];
    int n;

    cout << "Enter the number of students: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        a[i].getData();
    }

    cout << "\nStudent Details:\n";
    for (int i = 0; i < n; i++) {
        a[i].display();
    }

    return 0;
}
