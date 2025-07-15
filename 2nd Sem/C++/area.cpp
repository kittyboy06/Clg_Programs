#include<iostream>
using namespace std;

class rectangle {
private:
    int length,breadth, area;
public:
    void getData()
    {
        cout << "Enter the values for  length and breadth: ";
        cin >> length >> breadth;
    }

    void comp()
    {
        area = length * breadth;
    }

    void display()
    {
        cout << "Area of rectangle: " << area << endl;
    }
};

int main()
{
    rectangle r;
    r.getData();
    r.comp();
    r.display();
    return 0;
}