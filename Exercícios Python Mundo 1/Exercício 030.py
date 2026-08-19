from os import system
system('cls')

num = []
min = 0
max = 0

for i in range(3):
    numeros = int(input('Digite os números: '))
    num.append(numeros)
    if numeros > max: max = numeros
for i in num:
    min = max
    if i < min: min = i
    
print(f'O maior número é {max} e o menor número é {min}')

    