from os import system
system('cls')

lista_geral = []
lista_par = []
lista_impar = []
cont = 1

while True:
    user = int(input(f'Digite o {cont}ª valor: '))
    lista_geral.append(user)
    cont += 1
    
    escolha = str(input('Quer continuar? ')).upper().strip()
    if escolha == 'S':
        continue
    elif escolha == 'N':
        print('FIM DO PROGRAMA!')
        print('-='*40)
        break
print(f'A lista completa de números é: {lista_geral}')

for user in lista_geral:
    
    if user %2 == 0:
        lista_par.append(user)
        
    elif user %2 == 1:
        lista_impar.append(user)

print(f'A lista de números pares é: {lista_par}')
print(f'A lista de números ímpares é: {lista_impar}')

    