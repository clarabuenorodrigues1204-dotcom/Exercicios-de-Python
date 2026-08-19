from os import system
system('cls')

#Aumento no salário
salario = float(input('Digite o quanto você recebe: '))

if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print(f'O seu salário que era de R$ {salario} , com aumento de 10% passou a ser de R$ {aumento:.2f}')
else:
    aumento = salario + (salario * 15  / 100)
    print(f'O seu salario que antes era {salario}, com o aumento 15% será de R$ {aumento:.2f}')
      




      