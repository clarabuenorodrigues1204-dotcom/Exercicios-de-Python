from os import system
system('cls')

from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano = date.today().year
calculo_idade = ano - ano_nascimento

if calculo_idade <= 9:
    print(f'O atleta tem {calculo_idade} anos, e sua categoria ideal é a MIRIM')

elif calculo_idade <= 14:
    print(f'O atleta tem {calculo_idade} anos, e sua categoria ideal é a INFANTIL')

elif calculo_idade <= 19:
    print(f'O atleta tem {calculo_idade} anos , e sua categoria ideal é a JUNIOR ')

elif calculo_idade <= 25:
    print(f'O atleta tem {calculo_idade} anos, e sua categoria ideal é a SÊNIOR')

elif calculo_idade > 25:
    print(f'O atleta tem {calculo_idade} anos, e sua categoria ideal é a MASTER')