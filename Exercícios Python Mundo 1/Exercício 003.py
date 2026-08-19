#Calculadora de Idade
from datetime import date

nascimento = int(input('Qual seu ano de nascimento? '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print(f'Você tem {idade} anos')