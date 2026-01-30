#include <iostream>
using namespace std;
int main()
{
    double a, b, c;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    try
    {
        if (b == 0)
            throw 0;
        c = a / b;
        cout << a << " / " << b << " = " << c << endl;
    }
    catch (int e)
    {
        cerr << "Division by zero is not allowed." << endl;
    }
}