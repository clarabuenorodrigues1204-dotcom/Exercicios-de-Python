from os import system
system('cls')

nome = str(input('Digite seu nome completo: ')).strip()
print(f'O nome todo em letras maiúsculas é: {nome.upper()}')
print(f'O nome todo em letras minúsculas é: {nome.lower()}')
print(f'O nome {nome} tem o total de {len(nome)} de letras')
primeiro_nome = nome.split()[0]
print(f'O primeiro nome é: {primeiro_nome}')
print(f'O primeiro nome tem {len(primeiro_nome)} de letras')


