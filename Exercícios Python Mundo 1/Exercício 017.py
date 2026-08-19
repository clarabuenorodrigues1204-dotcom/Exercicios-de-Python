from os import system
system('cls')

from random import randint
from math import sin , cos , tan, radians

num_aleatorio = randint(1, 360)
sen = sin(radians(num_aleatorio))
coss = cos(radians(num_aleatorio))
tangen = tan(radians(num_aleatorio))
print(f'O SENO é: {sen:.2f} \n o COSSENO é: {coss:.2f} \n TANGENTE é: {tangen:.2f}')