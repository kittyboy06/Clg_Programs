#include<iostream>
using namespace std;

class item
{
    private:
        int number;
        float cost;
    public:
        void getdata(int a, float b);
        void putdata()
        {
            cout<<"Number: "<<number<<"\nCost: "<<cost<<endl;
        }
};

void item::getdata(int a, float b)
{
    number = a;
    cost = b;
}

int main()
{
    item i;
    i.getdata(1001, 29.99);
    i.putdata();
    return 0;
}