from os import system
system('cls')

from random import randint

print(f"{'=' * 40}\n{'ÍMPAR OU PAR':^40}\n{'=' * 40}")

soma = counter = 0

while True:
    valor = int(input('Digite um valor: '))
    print( "-" * 40)

    print("""ESCOLHA UMA OPÇÃO:
[1] - ÍMPAR
[2] - PAR""")
    
    jogador = int(input('Qual opção você escolhe? '))
    
    print( "-" * 40)
    
    if jogador > 2:
        
        print('OPÇÃO INVÁLIDA! JOGUE NOVAMENTE')
        continue
    
    computador = randint(0, 10)
    soma = valor + computador
    
    if jogador == 2 and soma % 2 == 0:
        print('O JOGADOR GANHOR')
        
    elif jogador == 1 and soma % 2 != 0:
        print('O JOGADOR GANHOR')
        
    else:
        print('O COMPUTADOR GANHOU!')
        break
    
    counter +=1
    
    print( "-" * 40)

    
    
print( "=" * 40)  
print(f'Você jogou {valor} e o computador jogou {computador}. A soma entre esses dois números é: {soma}')
print(f'O jogador ganhou {counter} consecutivas')      

    