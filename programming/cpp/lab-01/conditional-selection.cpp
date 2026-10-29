#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int a, b, c;
    cout << "Enter a: ";
    cin >> a;
    cout << "Enter b: ";
    cin >> b;
    cout << "Enter c: ";
    cin >> c;

    int result;


    if (a % 2 == 0 or b % 2 == 0 or c % 2 == 0) {
        result = max(a, (b, c));
        cout << "At least one number is even. Max = " << result << endl;
    } else {
        result = min(a, (b, c));
        cout << "No even number. Min = " << result << endl;
    }

    return 0;
}
