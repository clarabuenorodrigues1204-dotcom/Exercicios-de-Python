from os import system
system('cls')


soma = 0

for _ in range(6):
    numeros = int(input('Digite os números desejados: '))
    if numeros % 2 == 0:
        soma += numeros
print(soma)    