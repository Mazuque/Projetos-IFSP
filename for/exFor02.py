'Construir um algoritmo que leia a idade de N pessoas.'
'O sistema deve calcular: a média das idades, a menor e a maior idade informada'


#variaveis
qtd = 0
idade = 0
media = 0.0
menor = 0
maior = 0
soma = 0



#programa
qtd = int(input("informe a quantidade de pessoas que serão analisadas: "))

for contador in range(1,qtd+1,1):
    idade=int(input(f"Informe a idade: "))
    soma = soma+idade
    
    if contador == 1 : 
        maior = idade
        menor  = idade
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade


media= soma/qtd

print(f" A media das idades {media:,.2f}:")
print(f" Maior idade {maior}")
print(f" Menor idade {menor}")
