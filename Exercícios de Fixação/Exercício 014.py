from os import system
system('cls')

vogais = 'aeiouáéíóúàèìòùâêîôûãõ'
cont_vogal = cont_conso = 0
frase = str(input('Digite uma frase: ')).strip().lower()

cont_espaço = frase.count(" ")

#Verifica se há vogais e consoantes na frase, se sim faz suas devidas funções
for i in frase:
    if i in vogais:
        cont_vogal += 1
    elif i.isalpha():
        cont_conso += 1



print(f'A frase tem o total de {len(frase)} caracteres')
print(f'A quantidade de espaços nesta frase é: {cont_espaço}')
print(f'O total de vogais na frase é: {cont_vogal}')
print(f'O total de consoantes na frase é: {cont_conso}')
