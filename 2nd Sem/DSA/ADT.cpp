#include <iostream>
using namespace std;
#define MAX 100
int list[MAX], n = 0;
void insertAtEnd(int value) {
    if (n < MAX) {
        list[n] = value;
        n++;
    } else {
        cout << "List is full!" << endl;
    }
}

void insertAtPosition(int value, int position) {
    if (n >= MAX || position < 1 || position > n + 1) {
        cout << "Invalid position or list is full!" << endl;
        return;
    }
    for (int i = n; i >= position; i--) {
        list[i] = list[i - 1];
    }
    list[position - 1] = value;
    n++;
}
void deleteAtPosition(int position) {
    if (n == 0 || position < 1 || position > n) {
        cout << "Invalid position or list is empty!" << endl;
        return;
    }
    for (int i = position - 1; i < n - 1; i++) {
        list[i] = list[i + 1];
    }
    n--;
}

void display() {
    for (int i = 0; i < n; i++) {
        cout << list[i] << " ";
    }
    cout << endl;
}

void search(int value) {
    for (int i = 0; i < n; i++) {
        if (list[i] == value) {
            cout << "Element " << value << " found at position " << i + 1 << endl;
            return;
        }
    }
    cout << "Element " << value << " not found in the list." << endl;
}

void update(int oldValue, int newValue) {
    for (int i = 0; i < n; i++) {
        if (list[i] == oldValue) {
            list[i] = newValue;
            cout << "Element " << oldValue << " updated to " << newValue << endl;
            return;
        }
    }
    cout << "Element " << oldValue << " not found in the list." << endl;
}