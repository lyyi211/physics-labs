#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Circle {
private:
    double x, y, r;

public:
    // default constructor
    Circle() {
        x = 0;
        y = 0;
        r = 1;
        cout << "Default constructor" << endl;
    }

    // constructor with parameters
    Circle(double X, double Y, double R) {
        x = X;
        y = Y;
        setRadius(R);
        cout << "Constructor with parameters" << endl;
    }

    // copy constructor
    Circle(const Circle& other) {
        x = other.x;
        y = other.y;
        r = other.r;
        cout << "Copy constructor" << endl;
    }

    // destructor
    ~Circle() {
        cout << "Destructor" << endl;
    }

    void setX(double X) { x = X; }
    void setY(double Y) { y = Y; }

    void setRadius(double R) {
        if (R > 0)
            r = R;
        else
            r = 1;
    }

    double getX() const { return x; }
    double getY() const { return y; }
    double getRadius() const { return r; }

    double area() const {
        const double PI = 3.141592653589793;
        return PI * r * r;
    }

    double length() const {
        const double PI = 3.141592653589793;
        return 2 * PI * r;
    }

    void print() const {
        cout << "Circle: center (" << x << ", " << y
             << "), r = " << r
             << ", S = " << area()
             << ", L = " << length() << endl;
    }
};

int main() {
    int n;
    cout << "Number of circles (5..10) ";
    cin >> n;

    if (n < 5) n = 5;
    if (n > 10) n = 10;

    vector<Circle> circles;
    circles.reserve(n);

    cout << "Enter " << n << " circles (x, y, r):" << endl;

    for (int i = 0; i < n; i++) {
        double x, y, r;
        cin >> x >> y >> r;

        // створюЇмо обТЇкт одразу у вектор≥ Ч без окремого c
        circles.emplace_back(x, y, r);   // викликаЇтьс€ “≤Ћ№ » constructor with parameters
    }

    // ---------- Task 1: print all circles ----------
    cout << "\nAll circles:\n";
    for (const Circle& c : circles) {
        c.print();
    }

    // ---------- Task 2: total area ----------
    double totalArea = 0.0;
    for (const Circle& c : circles) {
        totalArea += c.area();   // +=, а не =+
    }
    cout << "\nTotal area of all circles = " << totalArea << endl;

    // ---------- Task 3: circle with largest radius ----------
    int iMax = 0;
    for (int i = 1; i < (int)circles.size(); i++) {
        if (circles[i].getRadius() > circles[iMax].getRadius()) {
            iMax = i;
        }
    }

    cout << "\nCircle with largest radius:\n";
    circles[iMax].print();

    return 0;
}
