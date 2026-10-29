#include <iostream>
using namespace std;

int main() {
    int N, M;
    cout << "Enter N: "; cin >> N;
    cout << "Enter M: "; cin >> M;

    if (N >= M) {
        cout << "Error: N must be less than M." << endl;
    } else {

        int i = N + 1;
        while (i < M) {
            if (i % 2 == 0)
                cout << i << " ";
            i++;
        }
    }

    return 0;
}
