from os import system
system('cls')

#Print especial
def escreva(txt):   
    tam = len(txt) + 4
    print('='* tam)
    print(txt.center(tam))
    print('='* tam)
    
escreva(txt = input('Escreva uma frase: '))