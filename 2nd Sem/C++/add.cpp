#include <iostream>
using namespace std;

class Addition {
    int a, b;

public:
    void getData() {
        cout << "Enter two numbers: ";
        cin >> a >> b;
    }

    void displaySum() {
        cout << "Sum: " << (a + b) << endl;
    }
};

int main() {
    Addition obj;
    obj.getData();
    obj.displaySum();
    return 0;
}
    