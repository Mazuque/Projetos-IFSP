'''
Faça um programa que receba o salario base de um funcionário.
Calcule e mostre o salário a receber, sabendo que esse funcionário tem gratificação
de R$ 50, 000 e paga imposto de 10% sobre o salário base.
'''

#variáveis
sal=0.0
salF=0.0
desc=0.0

#sal, salF, des = 0.0, 0.0, 0.0
sal = float(input("Informe o salário do funcionário"))

desc = sal*(10/100)

salF = sal + 50 - desc

print(f"O salário final é: R$ {salF}")
