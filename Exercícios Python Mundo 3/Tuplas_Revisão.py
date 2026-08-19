from os import system
system('cls')

tupla = ()
for i in range(5):
    numero = int(input('Digite um número: '))
    tupla = tupla + (numero,)          # concatena criando uma tupla nova
    tupla = tuple(sorted(tupla, reverse=True))  # "ordena" recriando a tupla

print(tupla)

# "inserindo" no início - já que não existe insert() em tupla
novo = int(input('Digite mais um número: '))
tupla = (novo,) + tupla
tupla = tuple(sorted(tupla, reverse=True))
print(tupla)

# testando outras funções de tupla
print(f'Quantidade de vezes que {novo} aparece: {tupla.count(novo)}')
print(f'Índice do valor {novo}: {tupla.index(novo)}')
print(f'Tamanho da tupla: {len(tupla)}')

# "removendo" um elemento - recriando a tupla sem ele
elemento_remover = tupla[0]
tupla = tupla[1:]  # fatiamento remove o primeiro elemento
print(f'Removido: {elemento_remover}')
print(tupla)

# esvaziando a tupla
tupla = ()
print(tupla)