#include <iostream>
using namespace std;

double solution(int n, double k) {
    if (n < 0) {
        return 0.0;
    }
    else if(n==0){
        return 1.0;
    }
    double num = 1.0;
    for(int i = 0; i < n; i++) {
        num *= k;
    }

    return num + solution(n - 1, k);
}
int main() {
   int n;
   double k;

    cout << "Enter number n : ";
    cin >> n;
    cout << "Enter k: ";
    cin >> k;

    cout << "Result: " << solution(n, k) << endl;

    return 0;
}
