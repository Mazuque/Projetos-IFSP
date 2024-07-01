'Uma escola está realizando matrícula para um curso aberto à comunidade, com limite de 20 vagas. Assumindo que os alunos são cadastrador por computador,'
'escreva um algoritmo que:'
' - leia a idade e o sexo do aluno;'
' - Informe que a turma está lotada, quando o número de inscritos atingir a quantidade de vagas;'
' - Mostre a idade média dos candidatos;'
' - Mostre a quantidade de mulheres inscritas;'
' - Mostre os candidatos (homens e mulheres) maiores de idade.'


#variaveis
qtd = 20
idade = 0
sexo = ""
qtdM = 0
maior = 0
soma = 0
media = 0.0

#programa
print(f" Matricula do Curso a comunidade [20 vagas]")

for contador in range(0,qtd,1):
    print(f" Informe os dados do Aluno {contador+1}")
    idade=int(input(f"Informe a idade: "))
    sexo=(input(f"Informe o sexo do candidato [H - Homem | M - Mulher]").upper())
    soma = soma+idade

    if sexo == "M": 
        qtdM = qtdM+1
    if idade >=18:
        maior = maior + 1
    

media= soma/qtd
print(f" TURMA LOTADA")
print(f" ")
print(f" - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print(f" A media das idades: {media:,.2f}:")
print(f" ")
print(f" Quantidade de mulheres inscritas: {qtdM}")
print(f" ")
print(f" Quantidade de maiores de idade: {maior}")


