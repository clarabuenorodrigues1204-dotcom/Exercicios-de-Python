from os import system
system('cls')

from random import randint

print("""Oi! Sou o seu computador...
Acabei de pensar em um número entre 0 e 10.
Consegue adivinhar qual foi? """)

num_aleatorio = randint(0, 10) #Faz o computador "pensar"
num = int(input('Qual é seu palpite? '))
contador = 0

while num != num_aleatorio:
    
    if num < num_aleatorio:
        print('Mais...Tente um número maior')
        
    elif num > num_aleatorio:
        print('Menos...Tente um número menor')
    num = int(input('Tente outro número: '))
    contador += 1
    

print(f'Você acertou depois de {contador} tentativas! O meu número escolhido foi {num_aleatorio} ')
        
