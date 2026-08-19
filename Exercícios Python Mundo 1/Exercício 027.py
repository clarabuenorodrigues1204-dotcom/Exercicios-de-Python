from os import system
system('cls')

distancia = float(input('Digite a distância da sua viagem: '))

if distancia <= 200:
 preço = distancia * 0.50
 print(f'O preço da sua passagem será de: R${preço:.2f}')
 
if distancia > 200:
    preço = distancia *0.45
    print(f'O preço da sua passagem será de: R${preço:.2f}')