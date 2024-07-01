'Crie em algoritmo que leia 10 números pelo teclado e exiba os números'
'na ordem inversa da que os números foram digitados'

#variaveis
cont = 0
vet = [0]*10

#algoritmo
for cont in range(0,10,1):
    vet[cont]=int(input(f"Informe o número para a posição {cont+1}: "))

for cont in range (9,0,-1):
    print(f"[{vet[cont]}]", end=' ')