#include<iostream>
using namespace std;

double areacircle(double rad)
{
    return 3.14 * rad * rad;
}

double arearectangle(double length, double breadth)
{
    return length * breadth;
}

double areasquare(double side)
{
    return side * side;
}

int main()
{
    double radius, length, breadth, side;
    int choice;

    

    while (true)
    {
        cout << "Choose the shape to calculate area:\n1. Circle\n2. Rectangle\n3. Square\n4. Exit\n";
        cout << "Enter your choice (1-4): ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            cout << "Enter radius of circle: ";
            cin >> radius;
            cout << "Area of Circle: " << areacircle(radius) << endl;
            break;
        case 2:
            cout << "Enter length and breadth of rectangle: ";
            cin >> length >> breadth;
            cout << "Area of Rectangle: " << arearectangle(length, breadth) << endl;
            break;
        case 3:
            cout << "Enter side of square: ";
            cin >> side;
            cout << "Area of Square: " << areasquare(side) << endl;
            break;
        case 4:
            cout << "Exiting the program." << endl;
            return 0;
        default:
            cout << "Invalid choice!" << endl;
        }
    }

    return 0;
}