#include <iostream>

using namespace std;

int main()
{
    int n;
    int *mas;
    cout<<"Enter the array size ";
    cin>>n;
    mas=new int[n];
    int i;
    cout<<"Enter array elements ";
    for(i=0; i<n; i++) cin>>mas[i];
    cout<<"MAS=";
    for(i=0; i<n; i++) cout<<mas[i]<<" ";
    cout<<endl;
    int *mas_changed=new int[2*n];
    cout<<"Changed array ";
    for(i=0;i<n; i++){
            mas_changed[2*i]=mas[i];
            mas_changed[2*1+1]=mas[i];
    }
    for(i=0; i<2*n; i++){
            cout<<mas_changed[i]<<" ";
    }
    delete[] mas;
    delete[] mas_changed;
    return 0;

}
