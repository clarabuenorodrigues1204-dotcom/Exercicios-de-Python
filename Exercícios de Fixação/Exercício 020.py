from os import system
system('cls')

while True:
    try:
        number = int(input('Digite um número: '))
        
        if number > 0 and number %2 == 0:
            print(f'O número {number} é Par Positivo')
        elif number < 0 and number %2 == 0:
            print(f'O número {number} é Par Negativo')
        elif number > 0 and number %2 == 1:
            print(f'O número {number} é Ímpar Positivo')
        elif number < 0 and number %2 == 1:
            print(f'O número {number} é Ímpar Negativo')
        else:
            print(f'É {number}')
        
        escolha = input('Quer continuar [S/N]? ').upper().strip()
        
    
        if escolha == 'N':
            break
        
        while escolha != 'N' and escolha != 'S':
            escolha = input('Somente [S/N]. Quer continuar? ')
        
        
    except ValueError:
        print('SOMENTE NÚMEROS INTEIROS')

    