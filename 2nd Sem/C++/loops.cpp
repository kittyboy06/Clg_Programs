#include<iostream>
using namespace std;

int main()
{
    //loops: for, while, do...while
    int c;
    cout<<"Enter a number: ";
    cin>>c;
    for (int i = 1; i <= c; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout<<"*";
        }
        cout<<endl;
    }

    cout<<"Enter a number: ";
    cin>>c;
    int i = 1;
    while (i <= c)
    {
        int j = 1;
        while (j <= i)
        {
            cout<<"*";
            j++;
        }
        cout<<endl;
        i++;
    }

    cout<<"Enter a number: ";
    cin>>c;
    i = 1;
    do
    {
        int j = 1;
        do
        {
            cout<<"*";
            j++;
        } while (j <= i);
        cout<<endl;
        i++;
    } while (i <= c);
    
}