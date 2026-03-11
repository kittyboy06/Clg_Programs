#include<iostream>
using namespace std;

class Vehicle
{
    public:
    int passengers;
};

class Road : virtual public Vehicle
{
    public:
    int Wheels;
    string VehicleName;
};

class Air : virtual public Vehicle
{
    public:
    int altitude;
    string airlineName;
};

class FlyingCar : public Road, public Air
{
    public:
    string brand;
    void getData() {
        cout << "Enter brand of the flying car: ";
        cin >> brand;
        cout << "Enter name of the road vehicle: ";
        cin >> VehicleName;
        cout << "Number of wheels: ";
        cin >> Wheels;
        cout << "Enter name of the airline: ";
        cin >> airlineName;
        cout << "Passengers in the aircraft: ";
        cin >> passengers;
        cout << "Altitude of the aircraft: ";
        cin >> altitude;
    }

    void display()
    {
        cout << "Brand of the flying car: " << brand << endl;
        cout << "Road Vehicle Name: " << VehicleName << endl;
        cout << "Passengers in the vehicle: " << passengers << endl;
        cout << "Number of wheels: " << Wheels << endl;
        cout << "Airline Name: " << airlineName << endl;
        cout << "Passengers in the aircraft: " << passengers << endl;
        cout << "Altitude of the aircraft: " << altitude << endl;
    }
};

int main()
{
    FlyingCar myFlyingCar;
    myFlyingCar.getData();
    myFlyingCar.display();
    return 0;
}