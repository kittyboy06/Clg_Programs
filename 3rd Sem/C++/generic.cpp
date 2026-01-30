#include<iostream>
using namespace std;

template <class T> class maximum
{
    public:
    T getmax(T a,T b,T c)
    {
        if (a>=b && a>=c)
        {
            return a;
        }
        else if (b>=a && b>= c)
        {
            return b;
        }
        else
        {
            return c;
        }
    }
};

int main()
{
    maximum<int> maxInt;
    maximum<float> maxFloat;
    maximum<char> maxChar;
    int a,b,c;
    cout<<"Enter three integers: ";
    cin>>a>>b>>c;
    cout<<"Maximum integer: "<<maxInt.getmax(a,b,c)<<endl;

    float x,y,z;
    cout<<"Enter three floats: ";
    cin>>x>>y>>z;
    cout<<"Maximum float: "<<maxFloat.getmax(x,y,z)<<endl;

    char ch1,ch2,ch3;
    cout<<"Enter three characters: ";
    cin>>ch1>>ch2>>ch3;
    cout<<"Maximum character: "<<maxChar.getmax(ch1,ch2,ch3)<<endl;

    return 0;
    
}