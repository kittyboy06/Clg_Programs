#include<iostream>
using namespace std;

void indexoutofrange()
{
    int i,n=5;
    int arr[5]={1,2,3,4,5};

    try
    {
        cout<<"Enter index to access array element (0-4): ";
        cin>>i;
        if(i>n-1 || i<0)
        {
            throw(i);
        }
        else
        {
            cout<<"Element at index "<<i<<" is "<<arr[i]<<"\n";
        }
    }
    catch(int e)
    {
        cout<<"Exception caught: Index "<<e<<" is out of range.\n";
    }
    
}

void divbyzero()
{
    int a,b;
    cout<<"Entert the values of a and b\n";
    cin>>a>>b;
    int x=a/b;
    try
    {
        if(x!=0)
        {
            cout<<"Result(a/x)="<<a/x<<"\n";

        }
        else
        {
            throw(x);
        }
    }
    catch(int i)
    {
        cout<<"Exception caught : x="<<x<<"\n";

    }
    cout<<"END";
}

int main()
{
    int ch;
    cout<<"1. Index Out of Range Exception\n2. Divide by Zero Exception\nEnter your choice: ";
    cin>>ch;
    switch(ch)
    {
        case 1:
            indexoutofrange();
            break;
        case 2:
            divbyzero();
            break;
        default:
            cout<<"Invalid choice!\n";
    }
    return 0;
}