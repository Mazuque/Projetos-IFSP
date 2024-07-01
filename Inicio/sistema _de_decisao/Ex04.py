'''
Desenvolver um algoritmo que solicite o nome e a idade de um nadador 
e imprima na tela o seu nome, a sua idade e em qual categoria ele está.

Idade                               Categoria
5 a 7                               Infantil A
8 a 11                              Infantil B
12 a 13                             Juvenil A
14 a 17                             Juvenil B
18 ou mais                          Adulto

Caso seja digitado uma idade fora das classes acima, informar
que o nadador não possui uma categoria válida
'''

#variaveis
idade=0
nome=""

nome = input("Insira o nome do(a) Nadador(a): ")
idade = int(input("Insira a sua idade: "))

if((idade>=5) and (idade<=7)):
    print(f"Nadador(a) {nome} de {idade} anos, está classificado na categoria Infantil A")
    
elif((idade>=8) and (idade<=11)):
    print(f"Nadador(a) {nome} de {idade} anos, está classificado na categoria Infantil B")
    
elif((idade>=12) and (idade<=13)):
    print(f"Nadador(a) {nome} de {idade} anos, está classificado na categoria Juvenil A")
    
elif((idade>=14) and (idade<=17)):
    print(f"Nadador(a) {nome} de {idade} anos, está classificado na categoria Juvenil B")
    
elif((idade>=18)):
    print(f"Nadador(a) {nome} de {idade} anos, está classificado na categoria Adulto")

else:
    print(f"Nadador(a) {nome} de {idade} anos, está em categoria INVÁLIDA")
