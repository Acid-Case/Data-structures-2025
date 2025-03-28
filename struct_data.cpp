#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <windows.h>

using namespace std;

vector<pair<int, int>> phi(int n) {
    vector<pair<int, int>> factors;
    for (int i=2; i*i<=n; ++i) {
        if (n % i == 0) {
            int cnt = 0;
            while (n % i == 0) {
                n /= i;
                cnt++;
            }
            factors.push_back({i, cnt});
        }
    }
    if (n > 1) {
        factors.push_back({n, 1});
    }
    return factors;
}

int main() {
    SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);
    cout << "====================================" << endl;
    cout << "Автор:  Борисов Данила Александрович" << endl; // Борисов Данила Александрович
    cout << "Группа: 090304-РПИа-o24" << endl;              // 090304-РПИа-o24
    cout << "====================================" << endl;

    int A, B = 0;
    cout << "Enter the first number: ";
    cin >> A;
    cout << "Enter the second number: ";
    cin >> B;

    auto factorsA = phi(A);
    auto factorsB = phi(B);

    int answer = 0;

    for (auto [p, alpha] : factorsA) {
        int beta = 0;
        for (auto [p_b, cnt_b] : factorsB) {
            if (p_b == p) {
                beta = cnt_b;
                break;
            }
        }
        if (beta == 0) {
            cout << -1 << endl;
            return 0;
        }
        int n = (alpha + beta - 1) / beta;
        answer = max(answer, n);
    }

    cout << "Answer is: " << answer << endl;
    return 0;
}
