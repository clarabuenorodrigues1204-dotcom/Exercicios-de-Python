from os import system
system('cls')

frase = str(input('Digite uma frase: ')).strip().lower().replace('', '')
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for i in range (len(junto) - 1, -1 , -1 ):
    inverso += junto[i]
    
if junto == inverso:
    print('É PALÍNDROMO')
else:
    print('Não é PALÍNDROMO')    