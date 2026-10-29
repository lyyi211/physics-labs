#include <iostream>
#include <vector>
using namespace std;

int main()
{
int n;
cout<<"Vector size: ";
cin>>n;

vector<int> v(n);
cout<<"Enter "<<n<<" numbers: ";
for (int i=0; i<n; i++) {
        cin >> v[i];
    }

vector<int> v2;
v2.reserve(2*n);
for (int i=0; i<n; i++) {
        v2.push_back(v[i]);
        v2.push_back(v[i]);
    }

cout<<"New vector: ";
for (int i=0; i<(int)v2.size(); i++) {
        cout<<v2[i]<< " ";
    }
return 0;
}
