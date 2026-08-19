from os import system
system('cls')

from time import sleep

print(f'{"CONTAGEM REGRESSIVA":=^40}')

for i in range(10 , -1, -1):
    print(i)
    sleep(1)

print(f'{"FIM!":=^40}')


#exercício curso em vídeo - for

for c in range(2, 51, 2):
     print(c)