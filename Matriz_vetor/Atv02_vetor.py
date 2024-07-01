'Crie em algoritmo que leia 30 números reais em um vetor e depois mostre'
'os números localizados nas posições impares'

#variaveis
cont = 0
vet = [0]*30

#algoritmo
for cont in range(0,30,1):
    vet[cont]=int(input(f"Informe o número para a posição {cont+1}: "))

for cont in range (0,30,1):
    if (cont%2 == 0):
        print(f"[{vet[cont]}]", end=' ')

    