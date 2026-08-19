from os import system
system('cls')

number = int(input('Digite um numero [999 - PARAR]: '))
counter = 0
total_sum = 0

while number != 999:
    counter += 1
    total_sum += number
    number = int(input('Digite um numero entre 0 e 999: '))
print(f'Foram digitados {counter} números')
print(f'A soma entre esses {counter} números é: {total_sum}')   
print('FIM DO PROGRAMA') 