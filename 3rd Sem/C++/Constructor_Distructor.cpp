#include <iostream>
using namespace std;

class stud
{
    int roll, per;
    public:
    stud()
    {
        cout << "Enter roll number and percentage: ";
        cin >> roll >> per;
        cout<<"Default constructor" << endl;
        cout<<"\t\tSTUDENT DETAILS" << endl;
        cout << "Roll Number: " << roll << endl;
        cout << "Percentage: " << per << endl;
    }
    stud(int r, int p)
    {
        roll = r;
        per = p;
        cout << "Parameterized constructor" << endl;
        cout<<"\t\tSTUDENT DETAILS" << endl;
        cout << "Roll Number: " << roll << endl;
        cout << "Percentage: " << per << endl;
    }
    stud(const stud &s)
    {
        roll = s.roll;
        per = s.per;
        cout << "Copy constructor" << endl;
        cout<<"\t\tSTUDENT DETAILS" << endl;
        cout << "Roll Number: " << roll << endl;
        cout << "Percentage: " << per << endl;
    }
    void display()
    {
        cout << "Roll Number: " << roll << endl;
        cout << "Percentage: " << per <<"%" << endl;
    }
    ~stud()
    {
        cout << "Destructor called for roll number: " << roll << endl;
    }
};

int main()
{
    int i,r;
    cout<<"Enter Roll Number and Percentage: ";
    cin>>r>>i;
    stud s1(r,i); // Parameterized constructor
    stud s2;
    stud s3(s1); // Copy constructor

    cout << "Details of Student 1:" << endl;
    s1.display();

    cout << "Details of Student 2:" << endl;
    s2.display();

    cout << "Details of Student 3 (Copy of Student 2):" << endl;
    s3.display();

    return 0;
}