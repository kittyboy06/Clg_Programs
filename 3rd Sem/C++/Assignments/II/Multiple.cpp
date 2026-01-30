#include<iostream>
using namespace std;

class Vehicle {
    public:
    int passengers;
};

class details
{
    public:
    string name;
    int age,phone;
};
class Car : public Vehicle, public details
{
    string brand;
public:
    void getData() {
        cout << "Enter brand of the car: ";
        cin >> brand;
        cout << "Passengers in the car: ";
        cin >> passengers;
        cout << "Name of the owner: ";
        cin >> name;
        cout << "Age of the owner: ";
        cin >> age;
        cout << "Phone number of the owner: ";
        cin >> phone;
    }
    void display() {
        cout << "Brand of the car: " << brand << endl;
        cout << "Passengers in the car: " << passengers << endl;
        cout << "Name of the owner: " << name << endl;
        cout << "Age of the owner: " << age << endl;
        cout << "Phone number: " << phone << endl;
    }
};
int main() 
{
    Car myCar;
    myCar.getData();
    myCar.display();
    return 0;
}