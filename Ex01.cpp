#include <cstdlib>
#include <iostream>
#include <locale.h>
#include <iomanip>

using namespace std;


int soma = 0;


int main(){
    setlocale(LC_ALL, "Portuguese");//linguagem


    int vetor [10];//vetor com 10 números
    for (int i=0; i<10; i++){ // "contador"
        cout<< "Digite o " << i+1 << " valor: "<<endl; //Mensagem 
        cin >> vetor[i]; //Coleta o valor
        soma += vetor[i]; //armazena a soma
    }

    cout<<"Os valores digitados são: "<<endl;
    for (int i=0; i<10; i++){
        cout << " | " << vetor[i] << " | "; // impressão do vetor
    }
        cout << endl;
        cout << "A cima dos valores digitados é: " << soma;
    return 0;
}
