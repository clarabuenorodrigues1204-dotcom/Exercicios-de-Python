from os import system
system('cls')

valor = ()
cont = cont2 = 0

for i in range(4):
    valores = int(input(f'Digite o {i + 1}° valor: '))
    
    valor += (valores,)
       
    if valores == 9:
        cont += 1      
print('-' * 40)   
print(f'Você digitou os valores: {valor}')    
print('-' * 40)

if 3 in valor:
    print(f'O número 3 apareceu na {valor.index(3) + 1}° posição') 
    print('-' * 40)
else:
    print('O número 3 não foi detectado na tupla')
       
for valores in valor:
    if valores % 2 == 0:
         cont2 += 1
         

print('-' * 40)
print(f'O número 9 apareceu {cont} vezes')
print('-' * 40)
print(f'Foram digitados {cont2} numeros pares')
print('-' * 40)

       

