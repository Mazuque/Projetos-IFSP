'criar um algoritmo que leia os elementos de uma matriz inteira 5x5 e escreva os elementos da diagonal principal'

#variáveis
linha = 0
coluna = 0
mat = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5 ]

#algoritmo
for linha in range (0,5,1):
    for coluna in range (0,5,1):
        mat[linha][coluna] = int(input(f"Informe o número para a posição {linha} {coluna}: "))

'imprimir a tabela inteira'
for linha in range (0,5,1):
    for coluna in range (0,5,1):
        print(f"[{mat[linha][coluna]}]", end=' ')
    print()

'imprimir apenas a diagonal princiapl'
for linha in range (0,5,1):
    for coluna in range (0,5,1):
        if (linha == coluna):
            print(f"[{mat[linha][coluna]}]", end=' ')
        else: 
            print(" ", end=' ')
    print()