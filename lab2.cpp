#include <iostream>
using namespace std;

int main() {
    int num = 0;
    cout << "Please enter a positive integer greater than 9: ";
    cin >> num;

    while (num <= 9) {
        cout << "Please enter a positive integer greater than 9: ";
        cin >> num;
    }

    int step = 0;
    cout << num;

    while (num > 9) {
        int sumOfDigits = 0;
        int temp = num;

        while (temp > 0) {
            int last_digit = temp % 10;
            sumOfDigits = sumOfDigits + last_digit;
            temp = temp/10;
        }

        num = sumOfDigits;
        step = step+1;
        cout << " - " << num<<endl;
    }

    cout << endl;
    cout << "Final value: " << num << endl;
    cout << "Total steps: " << step << endl;

    return 0;
}