from os import system
system('cls')

from random import randint

numeros = []

def sorteio():
    
    for i in range(1,6):
        
        computador = randint(0 , 10)
        numeros.append(computador)
        
    print(f'Os 5 números sorteados são: {numeros}')
    
    return numeros
sorteio()

def soma_par(numeros):
    pares = 0
    
    for numero in numeros:
        
        if numero %2 == 0:
            pares += numero
            
    return pares
   
print(f'A soma dos números pares sorteados é: {soma_par(numeros)}')