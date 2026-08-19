from os import system
system('cls')

velocidade = int(input('Digite a velocidade em que o carro está: '))


if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite de velocidade, você terá que pagar uma multa de R$ {multa:.2f}')
else:
    print('Você está na velocidade permitida, continue assim!')