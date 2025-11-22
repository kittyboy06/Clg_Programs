#include<iostream>
using namespace std;

class cons
{
    public:
    cons()
    {
        cout<<"Default Constructor Called"<<endl;
    }
    cons(int x)
    {
        cout<<"Parameterized Constructor Called with value: "<<x<<endl;
    }
    cons(cons &c)
    {
        cout<<"Copy Constructor Called"<<endl;
    }
};

int main()
{
    cons obj1;
    cons obj2(10);
    cons obj3(obj2);

    return 0;
}