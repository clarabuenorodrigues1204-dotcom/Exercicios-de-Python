from os import system
system('cls')

list_number = []
cont = 1
contador = 0 
while True:
    user = int(input(f'Digite o {cont}º número: '))
    cont += 1
    
    
    
    if user not in list_number:
        list_number.append(user)
    
    
    opcao = str(input('Quer continuar? ')).upper().strip()
    if opcao == 'S':
        continue
    elif opcao == 'N':
        break
    
print(f'A lista completa é: {list_number}')
print(f'A {len(list_number)} números dentro da lista')