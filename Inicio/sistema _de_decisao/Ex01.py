'''
EXEMPLO

'''
#variaveis
nome=""
situacao=0.0
nota1=0.0
nota2=0.0
media=0.0

#programa
nome = input("Informe o nome do Aluno: ")
nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))

media = (nota1+nota2)/2

if(media>=6):
    situacao = "APROVADO"
else:
    if((media>=4)and(media<6)):
        situacao = " DE RECUPERACAO"
    else:
        situacao = "REPROVADO"
        
print(f"{nome}, a sua média é: {media:,.2f} e você está {situacao}")