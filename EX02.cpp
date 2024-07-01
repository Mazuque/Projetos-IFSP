#include <cstdlib>
#include <iostream>
#include <locale.h>
#include <iomanip>

using namespace std;

int vetor [8];
int mult3 = 0;

int  main (){

    setlocale(LC_ALL,"portuguese");

    for(int i=0; i<8; i++){
        cout << "Digite o " << i+1 << " valor: "<< endl;
        cin >> vetor[i];
        
        if(vetor[i]%3 == 0){
            mult3++;
        }

    }
    cout << "os valores digitados são: " << endl;
    for(int i=0; i<8; i++){
        cout << " | " << vetor[i] << " | ";
    }
        cout << endl;
        cout << "Foram digitados " << mult3 << " números múltiplos de 3.";
    return 0;
}