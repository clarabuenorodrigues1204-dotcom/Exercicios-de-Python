from os import system
system('cls')


dinheiro = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = 5.22
print(f'Com R$ {dinheiro} que você tem na carteira, você consegue comprar US${dinheiro / dolar:.2f} ')

temp = float(input('Temperatura em °C: '))
f = 9 * temp / 5 + 32
print(f'A temperatura de °C {temp} em °F é de {f} ')