from os import system
system('cls')

lista_principal = []
lista_secundaria = []
count = 1

while True:
    
    user = int(input(f'Digite o {count}º valor: '))
    count += 1
    lista_principal.append(user)
    lista_principal = sorted(lista_principal)
    
    if user not in lista_secundaria:
        lista_secundaria.append(user)
        lista_secundaria = sorted(lista_secundaria)
    else: 
        print('Este número já existe na segunda lista')  
         
    escolha = str(input('Quer continuar? ')).strip().upper()
    
    if escolha == 'S':
        continue
    
    elif escolha == 'N':
        break
    else:
        print('Digite uma opção válida')
        escolha = str(input('Quer continuar? ')).strip().upper()
        
print(lista_principal)
print(lista_secundaria)