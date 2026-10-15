from os import system
system('cls')

soma = cont = 0


while True:
    try:
        number = int(input('Digite um número. [0] para o programa: '))
        soma += number
        if number == 0:
            break
        cont += 1
        

    except ValueError:
        print('APENAS NÚMEROS INTEIROS')
    
print('-'*30)

print(f'Foram digitados {cont} números')
print(f'A soma dos números digitados é {soma}')
if cont > 0:
    media = soma / cont
    print(f'A média é {media}')
elif cont == 0:
    print('Não há números para calcular há média')

print('-'*30)
    
    
        
    