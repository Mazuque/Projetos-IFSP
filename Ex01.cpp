#include <cstdlib>
#include <iostream>
#include <locale.h>
#include <iomanip>

using namespace std;


int soma = 0;


int main(){
    setlocale(LC_ALL, "Portuguese");//linguagem


    int vetor [10];//vetor com 10 n�meros
    for (int i=0; i<10; i++){ // "contador"
        cout<< "Digite o " << i+1 << " valor: "<<endl; //Mensagem 
        cin >> vetor[i]; //Coleta o valor
        soma += vetor[i]; //armazena a soma
    }

    cout<<"Os valores digitados s�o: "<<endl;
    for (int i=0; i<10; i++){
        cout << " | " << vetor[i] << " | "; // impress�o do vetor
    }
        cout << endl;
        cout << "A cima dos valores digitados �: " << soma;
    return 0;
}
