#include<iostream>
using namespace std;

class Employee {
    int empid;
    string name;
    float salary;
public:
    Employee()
    {
        empid = 0;
        name = "";
        salary = 0.0;
    }
    Employee(int id, string n, float sal)
    {
        empid = id;
        name = n;
        salary = sal;
    }
    Employee(const Employee &e)
    {
        empid = e.empid;
        name = e.name;
        salary = e.salary;
    }
    void display()
    {
        cout << "Employee ID: " << empid << endl;
        cout << "Name: " << name << endl;
        cout << "Salary: " << salary << endl;
    }
};

int main()
{
    Employee emp1;
    Employee emp2(1001, "Steve", 50000.0);
    Employee emp3(emp2);
    cout << "Details of Employee 1:" << endl;
    emp1.display();

    cout << "Details of Employee 2:" << endl;
    emp2.display();

    cout << "Details of Employee 3 (Copy of Employee 2):" << endl;
    emp3.display();
    return 0;
}