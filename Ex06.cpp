#include <iomanip>
#include <locale.h>
#include <iostream>
#include <cstdlib>

using namespace std;

int main() {
    int matriz[4][4];

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cout << "Digite o valor para a posição [" << i + 1 << "][" << j + 1 << "]: ";
            cin >> matriz[i][j];
        }
    }

    cout << "\nMatriz 4x4:\n"<<endl;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cout << matriz[i][j] << "\t";
        }
        cout << endl;
    }
    cout << endl;
    return 0;
}