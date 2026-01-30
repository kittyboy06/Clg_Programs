#include <iostream>
using namespace std;

class Stud
{
    public:
        static int count;
        Stud()
        {
            count++;
        }
};
int Stud::count = 0;
int main()
{
    Stud s1, s2, s3;
    cout << "Number of objects created: " << Stud::count << endl;
    return 0;
}