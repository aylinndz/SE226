#include <iostream>
using namespace std;

int main() {
    int n = 0;

    cout << "Please enter a number between 3 and 9: ";
    cin >> n;

    while (n < 3 || n > 9) {
        cout << "Please enter a number between 3 and 9: ";
        cin >> n;
    }

    int rows = (2 * n) - 1;

    for (int i = 1; i <= rows; i++) {

        int diff = n - i;
        if (diff < 0) {
            diff = -diff;
        }
        int level = n - diff;

        for (int j = 1; j <= level; j++) {
            cout << j;
        }
        cout << endl;
    }

    return 0;
}