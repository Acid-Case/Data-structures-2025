#include <iostream>
#include <cmath>
#include <limits.h>
#include <windows.h>

using namespace std;

int main() {
    SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);
    cout << "====================================" << endl;
    cout << "Автор:  Борисов Данила Александрович" << endl; // Борисов Данила Александрович
    cout << "Группа: РПИа-090304-o24" << endl;              // РПИа-090304-o24
    cout << "====================================" << endl;


    int A, B, i = 0;
    cout << "Enter the first number: ";
    cin >> A;
    cout << "Enter the second number: ";
    cin >> B;

    if (2 > A || 2e9 < A || 2 > B || 2e9 < B) {
        cout << "Invalid input. Please enter numbers from 2 to 2 * 10^9";
        cin >> i;
        return -1;
    }

    unsigned long long res = 1, max = ULLONG_MAX;
    for (; res != 0 && i < 64; i++) {
        if (res * B > max) {
            cout << "Number overflow" << endl;
            cout << "Answer is -1" << endl;
            cin >> i;
            return -1;
        }
        res = (res * B) % A;
    }
    i = i == 64 ? -1 : i;
    cout << "Answer is " << i << endl;
    cin >> i;
    return 0;
}
