#include<iostream>
#define MAX 100
int arr[MAX];
int n = 0;
using namespace std;

void add(int value) {
    if (n < MAX) {
        arr[n] = value;
        n++;
    } else {
        cout << "Array is full" << endl;
    }
}

void display() {
    if (n == 0) {
        cout << "Array is empty" << endl;
    } else {
        cout << "Array elements: ";
        for (int i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
}

void remove(int value) {
    int i;
    for (i = 0; i < n; i++) {
        if (arr[i] == value) {
            break;
        }
    }
    if (i < n) {
        for (int j = i; j < n - 1; j++) {
            arr[j] = arr[j + 1];
        }
        n--;
    } else {
        cout << "Value not found in array" << endl;
    }
}

int search(int value) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == value) {
            cout << "Value " << value << " found at index " << i << endl;
            return i;
        }
    }
    return -1;
}

void Create()
{
    cout << "Array created with size " << MAX << endl;
    n = 0;
    cout<<"Enter the number of elements you want to add: ";
    int count;
    cin >> count;
    cout << "You can now add elements to the array." << endl;
    for (int i = 0; i < count; i++)
    {
        int value;
        cin >> value;
        add(value);
    }
    
}

int main() {
    Create();
    display();
    
    int valueToRemove;
    cout << "Enter value to remove: ";
    cin >> valueToRemove;
    remove(valueToRemove);
    display();
    
    int valueToSearch;
    cout << "Enter value to search: ";
    cin >> valueToSearch;
    search(valueToSearch);
    
    return 0;
}

