#include <iostream>
using namespace std;

void area(int side)
{
    cout << "Area of square: " << side * side << endl;
}

void area(int length, int breadth)
{
    cout << "Area of rectangle: " << length * breadth << endl;
}

void area(double radius)
{
    cout << "Area of circle: " << 3.14 * radius * radius << endl;
}

int main()
{
   int ch;
    cout << "Choose shape to calculate area:\n1. Square\n2. Rectangle\n3. Circle\nEnter choice: ";
    cin >> ch;
    switch (ch)
    {
        case 1:
        {
            int side;
            cout << "Enter side of square: ";
            cin >> side;
            area(side);
            break;
        }
        case 2:
        {
            int length, breadth;
            cout << "Enter length and breadth of rectangle: ";
            cin >> length >> breadth;
            area(length, breadth);
            break;
        }
        case 3:
        {
            double radius;
            cout << "Enter radius of circle: ";
            cin >> radius;
            area(radius);
            break;
        }
        default:
            cout << "Invalid choice!" << endl;
    }
    return 0;
}