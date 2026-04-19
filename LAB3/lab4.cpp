#include <iostream>
using namespace std;
//1
void swapValues(int* p1, int* p2) {
    int temp = *(p1);
    *(p1) = *(p2);
    *(p2) = temp;
}
//2
void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *(arr + i) << " ";
    }
    cout << endl;
}
//3
int findMax(int* arr, int size) {
    int maxVal = *arr;
    for (int i = 1; i < size; i++) {
        if (*(arr + i) > maxVal) {
            maxVal = *(arr + i);
        }
    }
    return maxVal;
}
//4
void reverseArray(int* arr, int size) {
    int t;
    for (int i = 0; i < size / 2; i++) {
        t = *(arr + i);
        *(arr + i) = *(arr + size - i - 1);
        *(arr + size - i - 1) = t;
    }
}
//5
int* createArray(int size) {
    int* newArr = new int[size];
    return newArr;
}
//6
void deleteArray(int* arr) {
    delete[] arr;
    arr = nullptr;
}



int main() {
    cout << "Creating dynamic array..." << endl;
    int size;
    cout << "Enter array size: ";
    cin >> size;

    int* myArr = createArray(size);

    cout << "Enter values: ";
    for (int i = 0; i < size; i++) {
        cin >> *(myArr + i);
    }

    cout << "\nArray elements: ";
    printArray(myArr, size);

    int maxVal = findMax(myArr, size);
    cout << "Maximum element: " << maxVal << endl;

    cout << "----------------------------------" << endl;
    cout << "Swapping two numbers" << endl;
    int a = 5, b = 8;
    cout << "\nBefore swap a = " << a << " b = " << b << endl;

    swapValues(&a, &b);

    cout << "After swap a = " << a << " b = " << b << endl;

    cout << "----------------------------------" << endl;
    cout << "Reversing array..." << endl;

    reverseArray(myArr, size);

    cout << "\nArray after reverseArray: ";
    printArray(myArr, size);

    cout << "----------------------------------" << endl;
    cout << "Deleting array..." << endl;

    deleteArray(myArr);
    myArr = nullptr;

    return 0;
}
