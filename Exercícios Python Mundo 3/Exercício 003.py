from os import system
system('cls')

from random import randint

numeros = ()

for n in range(5):
    
    computador = randint(1,10)
    numeros += (computador,) 
    maior = max(numeros)
    menor = min(numeros)
    
print(f'Os valores sorteador foram: {numeros}')
print(f'O maior número sorteado é: {maior}')
print(f'O maior número sorteado é: {menor}')

