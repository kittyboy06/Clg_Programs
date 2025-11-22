#include <iostream>
using namespace std;

class Student {
public:
    static int totalStudents;

    Student() {
        totalStudents++;
    }

    static void displayCount() {
        cout << "Total Students: " << totalStudents << endl;
    }
};

int Student::totalStudents = 0;

int main() {
    Student s1, s2, s3;

    Student::displayCount();

    return 0;
}
