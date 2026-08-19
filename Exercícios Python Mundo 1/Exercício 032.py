from os import system
system('cls')

valores = []
for i in range(1):
    valores.append(int(input('Digite os valores: ')))
    calculo1 = valores[0] // 2 
    calculo2 = valores[0] % 2
print(calculo1 , calculo2)

