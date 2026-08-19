from os import system
system("cls")

#Antecessor e Sucessor
numero = int(input('Digite um número: '))
print(f'O antecessor é: {numero -1}')
print(f'O sucessor é: {numero +1}')

#Dobro, Triplo e raiz quadrada
n1 = int(input('Digite um número: '))
print(f'O dobro é {n1 * 2} o triplo é {n1* 3} e a raiz quadrada é {n1 ** (0.5):.2f}')