from os import system
system('cls')

lista_palavras = (
    'APRENDER',
    'PROGRAMAR',
    'PYTHON',
    'CURSO',
    'GRATIS',
    'ESTUDAR',
    'PRATICAR',
    'TRABALHAR',
    'MERCADO',
    'PROGRAMADOR',
    'FUTURO',
    
)

for palavra in lista_palavras:
    print(f'\nNa palavra "{palavra}" temos: ', end='') #A variável palavra criada no for serve como um "Posicionador" 
    
    for letra in palavra:  #verifica se na palavra tem as vogais "aeiou"
        if letra in 'AEIOU':
            print(letra, end='')
            
