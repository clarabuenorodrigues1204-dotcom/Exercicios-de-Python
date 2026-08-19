from os import system
system('cls')

#Tentiva de lógica nº2 - funciona parcialmente, mas há erro de lógica
lista_expressao = []
cont1 = 0
cont2 = 0
expressao = str(input('Digite uma expressão matemática: '))

for caractere in expressao:
    
    if caractere == '(':
        cont1 += 1
        lista_expressao.append(caractere)
        
    elif caractere == ')':
        cont2 += 1
        lista_expressao.append(caractere)
       
else: 
    if cont2 != cont1:
        print('Parênteses incorretos: Há aberturas sem fechamento')
        lista_expressao.pop()
    elif cont1 == cont2:
        print('Parênteses corretos!')

        

