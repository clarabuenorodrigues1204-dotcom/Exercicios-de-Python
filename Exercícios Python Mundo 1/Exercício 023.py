from os import system
system('cls')

frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra "A" aparece quantas vezes? {frase.count("a")}')
print(f'A letra "A" aparece a primeira vez na posição: {frase.find("a") +1 }')
print(f'A letra "A" aparece pela última vez na posição: {frase.rfind("a") +1 }')