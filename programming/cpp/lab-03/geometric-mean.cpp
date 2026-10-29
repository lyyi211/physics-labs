#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int x, y;
    int a=8;
    int N[a];

    cout<<"Enter 8 array elements separated by a space \n";
    for (int i=0; i<a; i++) {
        cin>>N[i];
        }
    cout<<"Your array \n";
    for (int i=0; i<a; i++) {
        cout<<N[i]<<" ";
        }
    int c=1;
    for (int i=0; i<a; i++) {
            c=c*N[i];
    }

    double g=0;
    cout<<endl;
    if (c>=0) {
            g=pow(c,1.0/a);
        }
        else {
                cout<<"Root expression less than 0 \n";
        return 0;
        }

        cout<<"Geometric mean of elements = "<<g<< endl;

        return 0;
}
