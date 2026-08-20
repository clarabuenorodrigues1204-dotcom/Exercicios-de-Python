from os import system
system('cls')

number = [[], []]
valor = 0

for i in range(1 , 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor %2 == 0:
        number[0].append(valor)
    else:
        number[1].append(valor)
        
number[0].sort()
number[1].sort()
    
print(number)  
