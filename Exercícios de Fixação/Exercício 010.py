from os import system
system('cls')

lista_geral = []
lista_par = []
lista_impar = []

while True:
    user = int(input('Digite um número: '))
    lista_geral.append(user)
    
    if user %2 == 0:
        lista_par.append(user)
    else:
        lista_impar.append(user)
           
    escolha = str(input('Quer continuar? ')).strip().upper()
    
    while escolha != 'S' and escolha != 'N':
       escolha = str(input('Quer continuar? ')).strip().upper()
    
    if escolha == 'S':
        continue
    elif escolha == 'N':
        break
    
print(f'A lista completa é: {lista_geral}')
print(f'A lista de números pares é {lista_par}')
print(f'A lista de números impares é {lista_impar}')
    
        