'''
Faça um programa que receba uma medida em pés
Faça as conversões a seguir em mostre os resultados.
a) polegadas
b) jardas
c) milhas

Sabe-se que:
    1 pé = 12 polegadas
    1 jarda = 3 pés
    1 milha = 1760 jardas
'''

#variaveis
pes=0.0
pol=0.0
jard=0.0
milh=0.0

pes = float(input("Insira o valor em pés para que seja convertido:"))

pol = (pes*12)

jard = (pes/3)

milh = (jard/1760)

print(f"O valor de {pes} equivale a: \n {pol} polegadas \n {jard:,.3f} Jardas \n {milh:,.5f} Milhas")