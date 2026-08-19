from os import system
system('cls')

#PROGRESSÃO ARITMÉTICA

a1 = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))

print(a1)

for _ in range(1, 10):
    a1 += razão
    print(a1)
print("FIM!")