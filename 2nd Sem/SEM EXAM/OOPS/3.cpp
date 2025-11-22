#include <iostream>
using namespace std;

class Circle
{
    private:
        double radius, area, circumference;
    public:
        Circle(double r)
        {
            radius = r;
        }
        void calculateArea()
        {
            area = 3.14 * radius * radius;
        }
        void calculateCircumference()
        {
            circumference = 2 * 3.14 * radius;
        }
        void display()
        {
            cout << "Radius: " << radius << endl;
            cout << "Area: " << area << endl;
            cout << "Circumference: " << circumference << endl;
        }
};

int main()
{
    double r;
    cout << "Enter radius of the circle: ";
    cin >> r;

    Circle c(r);
    c.calculateArea();
    c.calculateCircumference();
    c.display();

    return 0;
}