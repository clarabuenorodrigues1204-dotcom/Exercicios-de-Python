from os import system
system('cls')

lista_valores = []

cont = 0

while True:
    numeros = int(input('Digite um valor: '))
    lista_valores.append(numeros)
    cont += 1
    lista_valores.sort(reverse=True)
    
    opcao = str(input('Quer continuar [S/N]? ')).strip().upper()

    if opcao == 'S':
        continue
    elif opcao == 'N':
        print('-='*40)
        print('Fim do programa!')
        break
    
print('-='*40)
print(f'A lista de valores ordenada de forma decrescente são: {lista_valores}')
print('-='*40)
print(f'Foram digitados {cont} números')
print('-='*40)  

if 5 in lista_valores: #Verifica se o número 5 foi digitado
    print('O valor 5 foi encontrado na lista!')
    
else: 
    print('O valor 5 não foi encontrado na lista!')
    print('-='*40)
    

    


    