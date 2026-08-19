from os import system
system('cls')
valores = (1, 3, 4, 4, 5, 10, 2, 8, 9, 9, 2)

pos = []
maior = max(valores)
menor = min(valores)


user = int(input('Digite o valor desejado: '))
print('=-'*30)

if user in valores:
    print('Este número está dentro da tupla')
else:
    print('Este número não está dentro da tupla!')
   
print(f'O maior valor é {maior}\nE o menor valor é: {menor}')
print(f'O número {user} foi encontrado na tupla {valores.count(user)} vezes')

for p, v in enumerate(valores):
    if v == user:
        pos.append(p)

print(f'O número {user} foi encontrado nas posições {pos}')
        

