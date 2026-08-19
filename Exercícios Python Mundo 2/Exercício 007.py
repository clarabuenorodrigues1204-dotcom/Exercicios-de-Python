from os import system
system('cls')

retas = []

for _ in range(3):
    retas.append(float(input('Digite os valores dos segmentos: ')))
    
if retas[0] < retas[1] + retas[2] and retas[1] < retas[0] + retas[2] and retas[2] < retas[0] + retas[1]:
    print('DÁ PARA FORMAR UM TRIÂNGULO')
    
    if retas[0] == retas[1] == retas[2]:
        print('O TRIÃNGULO FORMADO FOI O EQUILÁTERO')

    elif retas[0] == retas[1] or retas[0] == retas[2] or retas[1] == retas[2]:
        print('O TRIÂNGULO FORMADO FOI O ISÓSCELES') 

    else:  
        print('O TRIÂNGULO FORMADO FOI O ESCALENO')
else:
    print('NÃO DA PRA FORMAR UM TRIÂNGULO')    
    
    