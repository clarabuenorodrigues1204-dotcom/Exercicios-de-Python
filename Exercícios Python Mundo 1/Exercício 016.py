from os import system
system('cls')

import math

cat1 = int(input('Digite o valor do cateto adjacente:  '))
cat2= int(input('Digite o valor do cateto oposto: '))
print(f'O comprimento da hipotenusa será {math.sqrt((cat1**2) + cat2 **2):.2f}')