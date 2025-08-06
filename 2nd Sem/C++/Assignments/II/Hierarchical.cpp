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
    string VehicleName;
    Road()
    {
        cout << "Creating a road vehicle." << endl;
    }
    void getData() {
        cout << "Enter name of the vehicle: ";
        cin >> VehicleName;
        cout << "Passengers in the vehicle: ";
        cin >> passengers;
        cout << "Number of wheels: ";
        cin >> Wheels;
    }
};

class Air : public Vehicle
{
    public:
    int altitude;
    string airlineName;
    Air()
    {
        cout << "Creating an air vehicle." << endl;
    }
    void getData() {
        cout << "Enter name of the airline: ";
        cin >> airlineName;
        cout << "Passengers in the aircraft: ";
        cin >> passengers;
        cout << "Altitude of the aircraft: ";
        cin >> altitude;
    }
};

int main()
{
    Road roadVehicle;
    roadVehicle.getData();
    cout << "Vehicle Name: " << roadVehicle.VehicleName << endl;
    cout << "Passengers in the vehicle: " << roadVehicle.passengers << endl;
    cout << "Number of wheels: " << roadVehicle.Wheels << endl;

    Air airVehicle;
    airVehicle.getData();
    cout << "Airline Name: " << airVehicle.airlineName << endl;
    cout << "Passengers in the aircraft: " << airVehicle.passengers << endl;
    cout << "Altitude of the aircraft: " << airVehicle.altitude << endl;

    return 0;
}