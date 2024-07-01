#include <iomanip>
#include <locale.h>
#include <iostream>
#include <cstdlib>

using namespace std;

int main(){

setlocale(LC_ALL,"portuguese");

int vetor1[3];
for(int i=0; i<3; i++){
    cout << "Digite o " << i+1<< "º valor do vetor 1: ";
    cin >> vetor1[i];
}

int vetor2[3];
for(int j=0; j<3; j++){
    cout << "Digite o " << j+1<< "º valor do vetor 2: ";
    cin >> vetor2[j];

}   

int calculo[3];
for(int k=0; k<3; k++){
    calculo[k] = vetor1[k]*vetor2[k];
}

cout << endl;

 //---------------------------------------------------------------------------------
cout << "Os valores digitados no vetor 1 são: ";
for(int i=0; i<3; i++){
    cout << " | "<< vetor1[i] << " | ";
}

cout << endl;

cout << "Os valores digitados no vetor 2 são: ";
for(int j=0; j<3; j++){
    cout << " | "<< vetor2[j] << " | ";
}

cout << endl;

cout << "Os valores dos vetores multiplicados são: ";
for(int k=0; k<3; k++){
    cout << " | " << calculo[k] << " | ";
}
    return 0;
}