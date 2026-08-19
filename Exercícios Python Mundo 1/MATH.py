from os import system
system('cls')


#"import math" importa toda a biblioteca
from math import sqrt, floor #usando o from --> nome da biblioteca --> import --> a função desejada (você importa somente a função que você quer)

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é {math.ceil (raiz):.2f}')