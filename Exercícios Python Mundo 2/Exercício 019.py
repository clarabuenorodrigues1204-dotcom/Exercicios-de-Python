from os import system
system('cls')

lista_peso = []

for p in range(1, 6):
   lista_peso.append(float(input(f'Qual o peso da {p}° pessoa: ')))
   
peso_menor = min(lista_peso)
peso_maior = max(lista_peso)

print(f'O maior peso é: {peso_maior}KG')
print(f'O menor peso é: {peso_menor}KG')
