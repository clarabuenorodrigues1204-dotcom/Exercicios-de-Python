from os import system
system('cls')

#Exercício 24 - curso em vídeo
nome = str(input('Digite o nome de uma cidade: ')).strip()
nome = nome.lower()
print(f'O nome da cidade começa com "Santo"? {nome.startswith("santo")}')

#Exercício 25 - curso em vídeo
nome2 = str(input('Qual é seu nome? ')).strip().lower()
print(f'A "Silva" nesse nome? {"silva" in nome2 }')