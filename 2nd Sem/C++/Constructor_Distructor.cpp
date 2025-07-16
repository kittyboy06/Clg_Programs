#include <iostream>
#include<string.h>
using namespace std;

class Student {
    char name[20];
    int roll;
    int marks;
    int phno;

public:
    Student(const char* n, int r, int m, int p) {
        strcpy(name, n);
        roll = r;
        marks = m;
        phno = p;
    }

    ~Student() {
        cout << "Destructor called for " << name << endl;
    }

    void displayData() {
        cout << "Name: " << name
             << ", Roll No: " << roll
             << ", Marks: " << marks
             << ", Phone No: " << phno << endl;
    }
};

int main() {
    Student s1("Alice", 101, 90, 1234567890);
    Student s2("Bob", 102, 85, 9876543210);

    s1.displayData();
    s2.displayData();

    return 0;
}
