#include <iostream>
using namespace std;

int main() {
    int N, M;
    cout << "Enter N: "; cin >> N;
    cout << "Enter M: "; cin >> M;

    if (N < M) {
        for (int i = N + 1; i < M; i++) {
            if (i % 2 == 0)
                cout << i << " ";
        }
    } else {
        cout << "Error: N must be less than M." << endl;
    }

    return 0;
}
