#include <iostream>
#include <cmath>
using namespace std;

float Myfunc(float x, float a)
{
    if (a - 2 == 0) {
        cout << "a - 2 = 0";
        return 1;
    }
    if (2 * x - a == 0) {
        cout << "2x - a = 0 if  x = " << x << endl;
        return 2;
    }
    if ((pow(a - x, 5) / pow(2 * x - a, 2)) < 0) {
        cout << "sqrt < 0 if x = " << x << endl;
        return 3;
    }

    float y = (pow(x, 3) + x + 3) / (a - 2) + sqrt(pow(a - x, 5) / pow(2 * x - a, 2));
    return y;
}

int main()
{
    float a, x1, x2, deltx;

    cout << "a=";
    cin >> a;
    cout << "x1=";
    cin >> x1;
    cout << "x2=";
    cin >> x2;
    cout << "deltx=";
    cin >> deltx;

    float y;

    for (float x = x1; x <= x2; x += deltx)
    {
        y = Myfunc(x, a);
        cout << "x = " << x << " ,y = " << y << endl;
    }

    return 0;
}
