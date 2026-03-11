#include<iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int add(int a, int b, int c) {
    return a + b + c;
}

float add(float a, float b) {
    return a + b;
}

int main()
{
    cout << "Addition of two integers (3, 4): " << add(2, 3) << endl;
    cout << "Addition of three integers (3, 4, 5): " << add(2, 3, 4) << endl;
    cout << "Addition of two floats (3.5, 4.5): " << add(2.5f, 3.7f) << endl;

    return 0;
}