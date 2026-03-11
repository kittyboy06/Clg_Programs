#include<fstream>
#include<iostream>
using namespace std;

int main() {
    ofstream outFile("file_OUTPUT.txt");
    outFile << "Hello, file!" << endl;
    outFile.close();

    ifstream inFile("file.txt");
    string line;
    while (getline(inFile, line)) {
        cout << line << endl;
    }
    inFile.close();

    return 0;
}
