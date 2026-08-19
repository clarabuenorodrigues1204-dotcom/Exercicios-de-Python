from os import system
system('cls')

#Tentiva de lógica nº1 - funciona e não há erro de lógica

lista_expressao = []

expressao = str(input('Digite uma expressão matemática: '))

for caractere in expressao: 
   
    if caractere == '(': #verifica se a '(' em expressão e adiciona na lista
        lista_expressao.append(caractere)
        
    elif caractere == ')': #Verifica se há parênteses sem fechadura correspondente '('
        if len(lista_expressao) == 0: #Len percorre a lista e verifica se ela está vazia
            print('Parênteses incorretos: Fechamento sem abertura correspondente')
            break
        lista_expressao.pop()
else:
    if len(lista_expressao) == 0: #Len percorre a lista e verifica se ela está vazia
        print('Parênteses corretos!')
    else:
        print('Parênteses incorretos: Há aberturas sem fechamento')
        