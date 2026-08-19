from os import system
system('cls')


print(f"""{'=-' * 21}
|  {" LISTA DE PREÇOS - MATERIAL ESCOLAR":^22}   |
{'=-' * 21}""")

lista_preço = (

'Lápis', '1.75',
'Borracha', '2.00',
'Caderno', '15.90',
'Estojo', '25.00',
'Transferidor', '4.20',
'Caneta', '1.50',
'Compasso', '9.99',
'Mochila', '120.50',
'Livros', '34.90'
    
    
    
)
for i in range(0, len(lista_preço), 2):
    print(f'| {lista_preço[i]:<20} | R$ {lista_preço[i + 1]:>12} |')
    print('-' * 43)
