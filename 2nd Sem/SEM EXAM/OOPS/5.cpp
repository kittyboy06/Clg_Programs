#include<iostream>
using namespace std;
template <class T> void Swap(T& a, T& b)
{
    T temp = a;
    a = b;
     b = temp;
}

int main()
{
    int num1 = 10, num2 = 20;
    cout<<"Before Swapping: num1 = "<<num1<<", num2 = "<<num2<<endl;
    Swap(num1,num2);
    cout<<"After Swapping: num1 = "<<num1<<", num2 = "<<num2<<endl;
    double d1 = 1.5, d2 = 4.5;
    cout<<"Before Swapping: d1 = "<<d1<<", d2 = "<<d2<<endl;
    Swap(d1,d2);
    cout<<"After Swapping: d1 = "<<d1<<", d2 = "<<d2<<endl;
}