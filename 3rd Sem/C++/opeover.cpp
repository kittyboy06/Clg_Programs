#include<iostream>
using namespace std;

class incr
{
    int n;
    public:
        void read()
        {
            cout << "Enter a number: ";
            cin >> n;
        }

        void operator +()
        {
            n++;
        }

        void operator --()
        {
            n--;
        }

        void display()
        {
            cout << "Increment: " << n << endl;
        }

        void print()
        {
            cout << "Decrement: " << n << endl;
        }

};

int main()
{
    incr obj;
    obj.read();
    +obj;
    obj.display();
    --obj;
    obj.print();
    
    return 0;
}