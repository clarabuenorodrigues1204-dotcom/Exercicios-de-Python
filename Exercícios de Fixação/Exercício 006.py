from os import system
system('cls')

lista = [6 , 7 , 2 , 5 , 8]

user = int(input('Digite um número: '))
if user in lista:
    lista.remove(user)
    lista = sorted(lista)
    print(lista)
    
elif user not in lista:
    print(f'Adicionando o número {user} na lista')
    lista.append(user)
    lista = sorted(lista)
    
    print(lista)