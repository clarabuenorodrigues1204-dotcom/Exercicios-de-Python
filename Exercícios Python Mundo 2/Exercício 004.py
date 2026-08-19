from os import system
system('cls')

from datetime import date

nascimento = int(input('Digite o ano em que você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
saldo = 18 - idade
saldo2 = idade - 18

if idade == 18:
    print(f'Você nasceu em {nascimento}, tem {idade} anos de idade em {ano_atual} \nJá chegou a hora de se alistar')

elif idade < 18:
    print(f'Você nasceu em {nascimento}, tem {idade} anos de idade em {ano_atual} \nVocê irá se alistar no ano de {ano_atual + saldo}')

elif idade > 18:
    print(f'Você nasceu em {nascimento}, tem {idade} anos de idade em {ano_atual} \nJá passou da hora de se alistar... Você deveria ter se alistado no ano de {ano_atual - saldo2}')
    

