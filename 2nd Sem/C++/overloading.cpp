#include<iostream>
using namespace std;

double areacircle(double radius) 
{
    return 3.14 * radius * radius;
}

double arearectangle(double length, double width) 
{
    return length * width;
}

double areasquare(double side) 
{
    return side * side;
}

int main() 
{
    int choice;
    double radius, length, width, side;

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
                cout << "Area of Circle: " << areacircle(radius) << endl;
                break;
            case 2:
                cout << "Enter length and width of the rectangle: ";
                cin >> length >> width;
                cout << "Area of Rectangle: " << arearectangle(length, width) << endl;
                break;
            case 3:
                cout << "Enter side of the square: ";
                cin >> side;
                cout << "Area of Square: " << areasquare(side) << endl;
                break;
            case 4:
                cout << "Exiting program." << endl;
                return 0;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    }
}