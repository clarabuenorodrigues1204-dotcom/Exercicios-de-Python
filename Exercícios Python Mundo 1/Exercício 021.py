from os import system
system('cls')

num = int(input('Digite um número: '))
unidade = num % 10
print(f'Unidade: {unidade}')
dezena = (num // 10) % 10
print(f'Dezena: {dezena}')
centena = (num // 100) % 10
print(f'Centena: {centena}')
milhar = num // 1000
print(f'Milhar: {milhar}')