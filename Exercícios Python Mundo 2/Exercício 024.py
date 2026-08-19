from os import system
system('cls')

fatorial = int(input('Digite o número que você quer o fatorial: '))

num = fatorial
resultado = 1

print(f'Calculando o fatorial de {fatorial}! = ', end='')

while num > 1:
    
    print(f'{num} x ', end='')
    resultado = resultado * num
    num -= 1
    
print(f'1 = {resultado}')