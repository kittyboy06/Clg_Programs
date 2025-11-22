#include<iostream>
using namespace std;

class Vechicle {
    public:
    int passengers;
};

class Car : public Vechicle
{
    string brand;
public:
void getData() {
    cout << "Enter brand of the car: ";
    cin >> brand;
    cout<<"Passengers in the car: ";
    cin >> passengers;
}
    void display()
    {
        cout << "Brand of the car: " << brand << endl;
        cout << "Passengers in the car: " << passengers << endl;
    }
};

int main() {
    Car myCar;
    myCar.getData();
    myCar.display();
    return 0;
}
