'foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa cidade, num determiando dia'
'Para cada casa visitada, é fornecido o número do canal ( 9, 12 23 ou 24)'
'   Para fazer um algoritmo que:'
'   - Leia um número indeterminado de dados, até que seja digitado o canal 0 (zero);'
'   - Calcule e mostrer a porcentagem de audiência de cada emissora;'
'   - Caso seja digitado algum canal fora dos apresentados acima, informar como outros canais;'
'   - 0 número 0 (zero) não pode ser considerado um canal'


#variaveis
canal = 1
c9 = 0
c12 = 0
c23 = 0
c40 = 0
cOutro = 0
cont = 0
aud9 = 0.0
aud12 = 0.0
aud23 = 0.0
aud40 = 0.0
audOu = 0.0

#algoritmo
while canal != 0:
    canal = int(input("Informe o canal mais consumido[ 9 | 12 | 23 | 40]:"))
    if canal == 9:
        c9 = c9+1
    elif canal == 12:
        c12 = c12+1
    elif canal == 23:
        c23 = c23+1
    elif canal == 40:
        c40 = c40+1
    elif canal > 0:
        cOutro = cOutro+1

cont = c9+c12+c23+c40+cOutro 

aud9 = (c9/cont)*100
aud12 = (c12/cont)*100
aud23 = (c23/cont)*100
aud40 = (c40/cont)*100
audOu = (cOutro/cont)*100

print(f" Resultado da pesquisa")
print(f" Audiencia do canal 9: {aud9}")
print(f" Audiencia do canal 12: {aud12}")
print(f" Audiencia do canal 23: {aud23}")
print(f" Audiencia do canal 40: {aud40}")
print(f" Audiencia de outros canais: {audOu}")