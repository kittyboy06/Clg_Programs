#include<iostream>
using namespace std;

class Complex
{
    float real, imag;
public:
Complex()
{}
    Complex(float r, float i)
    {
        real = r;
        imag = i;
    }
    Complex operator+(Complex c)
    {
        Complex temp;
        temp.real = real + c.real;
        temp.imag = imag + c.imag;
        return temp;
    }
    void display()
    {
        cout << real <<"+i"<< imag << endl;
    }
};

int main()
{
    Complex c1(2.1, 3.5), c2(1.6, 2.7);
    Complex c3 = c1 + c2;
    c1.display();
    c2.display();
    c3.display();
    return 0;
}