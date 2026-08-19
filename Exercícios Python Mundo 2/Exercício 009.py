from os import system
system('cls')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Você foi REPROVADO! Sua média foi {media}')

elif media >= 5.0 and media < 7.0:
    print(f'Você está de RECUPERAÇÃO! Sua média foi de {media}')

elif media >= 7.0:
    print(f'PARABÉNS! Você passou, sua média é de {media}')    