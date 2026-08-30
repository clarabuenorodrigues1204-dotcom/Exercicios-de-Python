from os import system
system('cls')

def area(b, h):
    calculo = b * h
    return calculo

b = float(input('Base: '))
h = float(input('Altura: '))

result = area(b , h)
print(f'A área do terreno é de {result} m²')
