from os import system
system('cls')

from random import choice, shuffle

nomes = []

for i in range(4):
    nomes.append(input('Digite os nomes dos alunos que irão apresentar: '))
    
shuffle(nomes)    

print(f'A ordem de apresentação será: {nomes}')