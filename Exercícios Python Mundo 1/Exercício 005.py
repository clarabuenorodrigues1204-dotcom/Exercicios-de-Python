from os import system
system('cls')


#Temperatura
temp = float(input('Temperatura em C°: '))
if temp < 15:
    print('Está frio!')
if temp >= 15 and temp <= 28:
    print('Temperatura agradável!')
if temp > 28:
    print('Esta quente!')
    
#Média Aritimética
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
media = (n1 + n2)/2
print(f'A média entre é {media}')

