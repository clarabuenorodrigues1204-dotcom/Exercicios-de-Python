from os import system
system('cls')

soma = 0

for i in range(1, 501):
    if i % 2 == 1 and i % 3 ==0:
        soma += i   
         
print(f'O resultado é: {soma}\n')

print(f'{'TABELA DE TABUADA':=^40}')
#Tabuada
n = int(input('Digite um número: '))
for i in range(1, 11):
 print(f'{n} x {i} = {n*i}')