#include<iostream>
using namespace std;

int main()
{
    // Branching
    int age;
    cout<<"Enter Your Age: ";
    cin>>age;
    if (age >= 18)
    {
        printf("Clg Student\n");
    }

    cout<<"Enter Your Age: ";
    cin>>age;
    if (age < 18)
    {
        printf("Scl Student\n");
    }
    else
    {
        printf("Clg Student\n");
    }
    
    cout<<"Enter Your Age: ";
    cin>>age;
    if (age < 18)
    {
        printf("Scl Student\n");
    }
    else if(age <= 22)
    {
        printf("Clg Student\n");
    }
    else
    {
        cout<<"Employe"<<endl;
    }
}