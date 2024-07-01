#include <iomanip>
#include <locale.h>
#include <iostream>
#include <cstdlib>

using namespace std;

int main() {
    setlocale(LC_ALL,"portuguese");

    float p1[15], p2[15], media[15];
    string situacao[15];

    for (int i = 0; i < 15; i++) {
        cout << "Digite a nota da P1 do aluno " << i + 1 << ": ";
        cin >> p1[i];
    }

    for (int i = 0; i < 15; i++) {
        cout << "Digite a nota da P2 do aluno " << i + 1 << ": ";
        cin >> p2[i];
    }

    for (int i = 0; i < 15; i++) {
        media[i] = (p1[i] + p2[i]) / 2.0;
        if (media[i] >= 6.0) {
            situacao[i] = "Aprovado";
        } else {
            situacao[i] = "Reprovado";
        }
    }
    cout << "\nResultados:\n" << endl;
    cout << "Aluno\tP1\tP2\tMédia\tSituação\n";
    for (int i = 0; i < 15; i++) {
        cout << i + 1 << "\t" << p1[i] << "\t" << p2[i] << "\t" << media[i] << "\t" << situacao[i] << endl;
    }

    return 0;
}
