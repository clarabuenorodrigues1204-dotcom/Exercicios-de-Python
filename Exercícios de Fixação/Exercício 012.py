from os import system
system('cls')

print(f'{'=-'*7}LISTA DE PREÇOS{'-='*7}')

lista_preços = [
   
['Arroz' , 10.50 ]   ,
['Feijão' , 9.99 ]   ,
['Macarrão' , 5.30 ]   ,
['Molho de tomate' , 1.99 ]   ,
['Refrigerante' , 8.00 ]  
   
]
lista_valor = []

for i in range(0, len(lista_preços)):
    print(f'| {lista_preços[i][0]:<20} | R$ {lista_preços[i][1]:>12} |')
    print('-' * 43)

for p, v in enumerate(lista_preços):
   lista_valor.append(v[1])
 
maior = max(lista_valor)
menor = min(lista_valor)

for produto in lista_preços:
    if produto[1] == maior:
        produto_maior = produto[0]

    if produto[1] == menor:
        produto_menor = produto[0]
 
  
somas = sum(lista_valor)
print(f'O produto mais caro é o {produto_maior} que custa R${maior:.2f}')
print(f'O produto mais barato é o {produto_menor} que custa R${menor:.2f}')
print(f'A soma total dos produtos é: R${somas:.2f}')