from os import system
system('cls')

from datetime import date

print(f'{'Maior e Menos de idade':=^40}')

ano_atual = date.today().year
contador = 0
contador2 = 0

for pessoa in range(1,8):
    
    nascimento = int(input(f'Em que ano a {pessoa}° nasceu? '))
    idade = ano_atual - nascimento
    
    if idade >= 18:
        contador += 1
        
    elif idade < 18:
        contador2 += 1
       
print(f'O número de pessoas que atingiram a maior idade são: {contador}')        
print(f'O número de pessoas que ainda não atingiram a maior idade são: {contador2}')