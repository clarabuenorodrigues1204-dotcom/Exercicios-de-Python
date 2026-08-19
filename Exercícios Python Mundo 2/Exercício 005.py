from os import system
system('cls')

nota = []

for i in range(2):
    nota.append(float(input('Digite suas notas: ')))
media = (nota[0] + nota[1])/ 2

if media < 5.0:
    print(f'REPROVADO! sua média foi de: {media:.1f}')  

elif media >= 5.0 and media < 7.0:
    print(f'Você está de RECUPERAÇÃO, sua média foi de: {media:.1f}') 

elif media >= 7.0:
    print(f'APROVADO! Parabéns, sua média foi de: {media:.1f}')