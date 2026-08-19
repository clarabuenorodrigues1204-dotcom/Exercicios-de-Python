from os import system
system('cls')

lista_number = []

while True:
    user = int(input('Digite um número: '))
    
    
    if user not in lista_number:
        lista_number.append(user)
        lista_number = sorted(lista_number)
        
    else:
        print('Esse número já entra dentro da lista! Digite outro')
    
    if len(lista_number) == 6:
        break
print(lista_number)