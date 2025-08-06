#include<iostream>
using namespace std;

class Vehicle
{
    public:
    int passengers;
};

class Road : public Vehicle
{
    public:
    int Wheels;
};

class Car : public Road
{
    string brand;
public:
    void getData() {
        cout << "Enter brand of the car: ";
        cin >> brand;
        cout << "Passengers in the car: ";
        cin >> passengers;
        cout << "Number of wheels: ";
        cin >> Wheels;
    }
    void display() {
        cout << "Brand of the car: " << brand << endl;
        cout << "Passengers in the car: " << passengers << endl;
        cout << "Number of wheels: " << Wheels << endl;
    }
};

int main()
{
    Car myCar;
    myCar.getData();
    myCar.display();
    return 0;
}
