from os import system
system('cls')

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Olá {nome} é um prazer te conhecer!')
print(f'O seu primeiro nome é: {nome.split()[0]}')
print(f'O seu último nome é: {nome.split()[-1]}')