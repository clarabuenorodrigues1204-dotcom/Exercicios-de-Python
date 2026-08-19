from os import system
system('cls')

contagem = ('zero', 'um', 'dois' ,'três', 'quatro', 'cinco', 'seis','seta', 'oitro', 'nove', 'dez')

while True:
    number = int(input('Digite um número entre 0 e 10: '))
    if 0 <= number <= 10:
        break
    print('Tente novamente. ', end='')
    print(f'Você digitou o número {contagem[number]}')
    
    