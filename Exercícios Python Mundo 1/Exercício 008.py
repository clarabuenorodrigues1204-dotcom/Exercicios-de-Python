from os import system
system("cls")

#DESCONTO
preço = float(input('Digite o valor do produto: '))
desc = preço - (preço*5 / 100)
print(f'O produto que antes custava R$ {preço} com desconto ele irá custar R$ {desc:.2f}')

#Aumento no salário
salario = float(input('Digite o quanto você recebe: '))
salario2 = salario + (salario * 15 / 100)
print(f'O seu salário que era de R$ {salario} , com aumento de 15% será de R$ {salario2:.2f}')