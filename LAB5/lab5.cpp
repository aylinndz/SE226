#include <iostream>
using namespace std;

double solution(int n, double k) {
    if (n < 0) {
        return 0.0;
    }
    double num = 1.0;
    for(int i = 0; i < n; i++) {
        num *= k;
    }

    return num + solution(n - 1, k);
}
int main() {
    cout << solution(5, 3) << endl;
    return 0;
}
