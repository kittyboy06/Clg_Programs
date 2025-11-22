#include<iostream>
using namespace std;

double area(double radius) 
{
    return 3.14 * radius * radius;
}

double area(double length, double width) 
{
    return length * width;
}

double area(int side) 
{
    return side * side;
}

int main() 
{
    int choice,side;
    double radius, length, width;

    cout << "Choose a shape to calculate area:\n1. Circle\n2. Rectangle\n3. Square\n4. Exit\n";

    while (true) 
    {
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) 
        {
            case 1:
                cout << "Enter radius of the circle: ";
                cin >> radius;
                cout << "Area of Circle: " << area(radius) << endl;
                break;
            case 2:
                cout << "Enter length and width of the rectangle: ";
                cin >> length >> width;
                cout << "Area of Rectangle: " << area(length, width) << endl;
                break;
            case 3:
                cout << "Enter side of the square: ";
                cin >> side;
                cout << "Area of Square: " << area(side) << endl;
                break;
            case 4:
                cout << "Exiting program." << endl;
                return 0;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    }
}