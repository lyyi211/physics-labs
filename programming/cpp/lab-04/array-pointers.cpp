#include <iostream>

using namespace std;

int main()
{
    int n;
    int i;
    int *mas;
    cout<<"Enter the array size ";
    cin>>n;
    mas=new int[n];
    int *p=mas;
    cout<<"Enter array elements ";
    for (i=0; i<n; i++, p++) {
        cin>>*p;
    }
    int *mas_changed=new int[2*n];
    int *from = mas;
    int *to = mas_changed;
    for(i=0; i<n; i++) {
        *to++=*from;
        *to++=*from;
        from++;
    }
    cout<<"Changed array \n";
    for(i=0; i<2*n; i++) {
        cout<<*(mas_changed+i)<<" ";
    }
    delete[] mas;
    delete[] mas_changed;

    return 0;
}

