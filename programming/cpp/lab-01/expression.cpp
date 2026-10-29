#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    float a, x, y;

    cout << "Enter x: ";
    cin >> x;
    cout << "Enter a: ";
    cin >> a;

    if (a - 2 == 0) {
        cout << "Error: a - 2 = 0, division by zero" << endl;
        return 1;
    }


    if (2*x - a == 0) {
        cout << "Error: 2*x - a = 0, division by zero" << endl;
        return 2;
    }


    float c = pow(a - x, 5) / pow(2*x - a, 3);


    if (c < 0) {
        cout << "Error: square root < 0" << endl;
        return 3;
    }


    y = (pow(x, 3) + x + 3) / (a - 2) + sqrt(c);

    cout << "y = " << y << endl;

    return 0;
}
