#include <iostream>
using namespace std;

int main() {
    int n = 0;

    cout << "Please enter a number between 10 and 100: ";
    cin >> n;

    while (n < 10 || n > 100) {
        cout << "Invalid input. Please enter a number between 10 and 100: ";
        cin >> n;
    }

    int fizz = 0;
    int buzz = 0;
    int FizzBuzz = 0;

    for (int i = 1; i <= n; i++) {
        if (i % 7 == 0) {
            cout << i << " is skipped" << endl;
            continue;
        }
        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            FizzBuzz = FizzBuzz + 1;
        }
        else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizz = fizz + 1;
        }
        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzz = buzz + 1;
        }

        else {
            cout << i << endl;
        }
    }
    cout << "Fizz: " << fizz << endl;
    cout << "Buzz: " << buzz << endl;
    cout << "FizzBuzz: " << FizzBuzz << endl;

    return 0;
}