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
    string VehicleType;
};

class RoadVehicle : public Road
{
    string brand;
public:
    void getData() 
    {
        cout << "Enter brand: ";
        cin >> brand;
        cout << "Passengers: ";
        cin >> passengers;
        cout << "Vehicle Type: ";
        cin >> VehicleType;
    }
    void display() 
    {
        cout << "Brand: " << brand << endl;
        cout << "Passengers: " << passengers << endl;
        cout << "Vehicle Type: " << VehicleType << endl;
    }
};

int main()
{
    RoadVehicle myCar;
    myCar.getData();
    myCar.display();
    return 0;
}
