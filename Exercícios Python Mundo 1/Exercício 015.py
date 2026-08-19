from os import system
system('cls')

import math

num = float(input('Digite um número: '))
num2 = math.trunc (num)
print(f'O número {num} tem a porção inteira {num2}')