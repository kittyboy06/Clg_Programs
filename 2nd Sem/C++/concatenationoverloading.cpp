#include<iostream>
#include<string.h>
using namespace std;

class String
{
private:
    char str[20];
public:
    void input()
    {
        cout << "Enter a string: ";
        cin >> str;
    }
    void display()
    {
        cout << "String: " << str << endl;
    }
    String operator+(String s)
    {
        String obj;
        strcat(str, s.str);
        strcpy(obj.str, str);
        return obj;
    }
};

int main()
{
    String s1, s2, s3;
    s1.input();
    s2.input();
    s3 = s1 + s2;
    s3.display();
    return 0;
}