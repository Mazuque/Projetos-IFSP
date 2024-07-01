

#variaveis
numero = 0

#programa
numero = int(input("informe o número para a tabuada: "))

for contador in range(1,11,1):
    print(f"{numero}x{contador} = {numero * contador}")