from os import system
system('cls')

from random import randint
from time import sleep
cont = 0
palpites = []
jogos = []
jogador = int(input('Digite o número de palpites: '))

for i in range(jogador):
    while True:
        num = randint(1,60)
        if num not in palpites:
            palpites.append(num)
            cont += 1
        if cont >= 6:
            cont = 0
            break
    jogos.append(palpites[:])
    palpites.clear()
    
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')