from os import system
system('cls')

import random

nome_alunos = []

for i in range (4):
 nome_alunos.append(input('Digite os nomes: '))

sorteio = random.randint(0, len(nome_alunos))       

print(f'O aluno sorteado foi {nome_alunos[sorteio]}')