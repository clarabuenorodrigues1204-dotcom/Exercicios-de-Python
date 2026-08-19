from os import system
system('cls')

dias = int(input('Por quantos dias ele foi alugado? '))
km = float(input('Quantos km foram percorridos pelo carro alugado? '))
carro = (60 * dias) + km * 0.15
print(f'O valor a pagar é {carro:.2f}')