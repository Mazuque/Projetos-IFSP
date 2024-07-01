'''
Construa um algoritmo que determine quanto será gasto para encher o tanque de um carro.
O Usuário forncerá os seguintes dados: Tipo de Carro (TC) (G -Gasolina / A-Álcool) e 
Capacidade do tanque (CT), em litros. Após a escolha do tipo de veículo e da capacidade do tanque,
o sistema irá imprimir uma mensagem falando o tipo do carro (G ou A) e pedirá para o usuário informar o valor do preço do litro do combustível.
Como saída, será informado para o usuário, o valor, em reais, do preço de se encher o tanque de combustível.
'''
import sys

#variaveis
tc = ""
ct = 0.0
precol = 0.0
tanquecheio = 0.0

tc=input("Informe o tipo de combustivel desejar colocar em seu carro [G - Gasolina | A - Álcool]: ").upper()

if((tc!= "A") and (tc != "G")):
    print("CÓDIGO INFORMADO INVÁLIDO")
    sys.exit()
    
ct=float(input("Informe a capacidade do tanque: "))


if(tc=='G'):
    print(f"O veiculo a ser abastecido a Gasolina possui um tanque de {ct} litros")
else:
    print(f"O veiculo a ser abastecido a Álcool possui um tanque de {ct} litros")

precol = float(input("Informe o valor do litro do combustível: "))

tanquecheio = precol*ct

print(f"O total a ser gasto para enche ro tanque será de R${tanquecheio:,.2f} ")


