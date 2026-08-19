from os import system
system('cls')

#1 - Contagem e classificação

cont1 = cont2 = cont3 = cont4 = 0

for i in range(1,9):
    number = int(input(f'Digite o {i}ª número: '))
    
    if number %2 == 0:
        cont1 += 1
            
    elif number %2 == 1:
        cont2 += 1
        
    if number > 0:
        cont3 += 1     
        
    elif number < 0:
        cont4 += 1
            
      
print(f'O total de números pares digitados foram: {cont1}')
print(f'O total de números impares digitados foram: {cont2}')
print(f'O total de números positivos digitados foram: {cont3}')
print(f'O total de números negativos digitados foram: {cont4}')


    