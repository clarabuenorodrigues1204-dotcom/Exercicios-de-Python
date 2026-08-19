from os import system
system('cls')

numeros = []

for i in range(2):
    numeros.append(int(input('Digite os números: ')))

if numeros[0] > numeros[1]:
    print('O primeiro valor é maior')
 
if numeros[1] > numeros[0]:
    print('O segundo valor é maior')

if numeros[0] == numeros[1]:
    print('Não existe valor maior, os dois valores são iguais')
