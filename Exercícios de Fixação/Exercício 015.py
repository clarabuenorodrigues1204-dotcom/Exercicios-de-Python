from os import system
system('cls')

print(f'{'='*8}VERIFICADOR DE PALÍNDROMO{'='*8}')

vogais = 'aeiouáéíóúàèìòùâêîôûãõ'
cont_vogal = cont_conso = 0

frase = str(input('Digite uma frase: ')).strip().lower().replace('', '')

palavras = frase.split() #split() transforma a frase em uma lista
junto = ''.join(palavras) #join() vai juntar as palvras da frase
inverso = '' 

for i in range (len(junto) - 1, -1 , -1 ):
    inverso += junto[i] #é um acumulador de string.
    
if junto == inverso:
    
    print(f'{'-'*40}')
    print('É PALÍNDROMO')
    print(f'{'-'*40}')
    
else:
    
    print(f'{'-'*40}')
    print('Não é PALÍNDROMO')  
    print(f'{'-'*40}')
    
for i in frase:
    if i in vogais:
        cont_vogal += 1
    elif i.isalpha():
        cont_conso += 1



print(f'A frase tem o total de {len(frase)} caracteres contando com os espaços')
print(f'{'-'*40}')
print(f'O total de vogais na frase é: {cont_vogal}')
print(f'{'-'*40}')
print(f'O total de consoantes na frase é: {cont_conso}')

