'''
Você está fazendo um trabalho de classificação de solo. Após colher uma amostra e verificar
a quantidade de pontos de água presente nela, classificou a amostra em:
    ROCHOSA: Se ao menos ou igual a 10 pontos de água
    FIRME: Se mais de 10 e menor ou igual a 40 pontos
    PANTANOSA: Se mais de 40 e mnor ou igual a 80 pontos
    QUANTIDADE INVÁLIDA: Se mais do que 80 pontos    
'''

#variaveis
qtdamostra = 0

qtdamostra=int(input("Quantos pontos de água foram coletados? "))

if(qtdamostra<=10):
    print("O solo é classificado como ROCHOSO")
else:
    if((qtdamostra >10) and (qtdamostra<= 40)):
        print("O solo é classificado como FIRME")
    else:
        if((qtdamostra >40) and (qtdamostra<= 80)):
            print("O solo é classificado como PANTANOSO")
        else:
            print("QUANTIDADE INVÁLIDA")

#forma2           
if(qtdamostra<=10):
    print("O solo é classificado como ROCHOSO")
    
elif((qtdamostra >10) and (qtdamostra<= 40)):
    print("O solo é classificado como FIRME")
    
elif((qtdamostra >40) and (qtdamostra<= 80)):
    print("O solo é classificado como PANTANOSO")
    
else:
    print("QUANTIDADE INVÁLIDA")            
