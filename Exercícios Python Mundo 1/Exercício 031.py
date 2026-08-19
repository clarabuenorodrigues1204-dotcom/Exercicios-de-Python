from os import system
system('cls')

#reta = float(input('Digite o número de uma reta: '))
#reta2 = float(input('Digite o número da segunda reta: '))
#reta3 = float(input('Digite o número da terceira reta: '))

#soma = reta + reta2
#if soma > reta3:print(f'DA PRA FORMAR UM TRIÂNGULO ')

#if soma < reta3:print(f'NÃO DA PRA FORMAR UM TRIÂNGULO')

retas = []

for _ in range(3):
    retas.append(float(input('Digite o valor das retas: ')))
if retas[0] < retas[1] + retas[2] and retas[1] < retas[0] + retas[2] and retas[2] < retas[0] + retas[1]:
    print('DÁ PARA FORMAR UM TRIÂNGULO')
else:
    print('NÃO DA PRA FORMAR UM TRIÂNGULO')    
    