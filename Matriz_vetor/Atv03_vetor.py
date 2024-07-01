'faça um algortimo que leia 50 valores reais e armazene em um vetor'
'modifique o vetor de modo que os valores das posições impares sejam aumentados em 5%, '
'e os das posições pares sejam aumentados em 2%. Imprima depois o vetor original e o resultante'

#variaveis
cont = 0
vet = [0.0]*10

#algoritmo
for cont in range(0,10,1):
    vet[cont]=int(input(f"Informe o número para a posição {cont+1}: "))


print( )


for cont in range (0,10,1):
    print(f"[{vet[cont]}]", end=' ')


print( )
print('Aplicando porcentagens')


for cont in range (0,10,1):
    if (cont%2 == 0):
        print(f"[{vet[cont]*1.05 :.3f}]", end=' ')
    else:
        print(f"[{vet[cont]*1.02 :.3f}]", end=' ')

