from os import system
system('cls')

from random import randint

num_aleatorio = randint(0, 5) #Faz o computador "pensar"
num = int(input('Digite um número: '))

if num == num_aleatorio:
    print('Você acertou')
    
else:
    print(f'Você errou! O número correto era {num_aleatorio}')

