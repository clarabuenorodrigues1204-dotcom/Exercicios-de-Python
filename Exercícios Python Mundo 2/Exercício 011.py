from os import system
system('cls')

from random import randint
from time import sleep

def jokenpo():
    print('JO')
    sleep(0.4)
    print('KEN')
    sleep(0.4)
    print('PÔ!!!!')
    sleep(0.4)

print('{:=^40}'.format(' JOKENPÔ '))

jogador = int(input('''ESCOLHA UMA OPÇÃO:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual é a sua jogada? '''))

if jogador < 0 or jogador > 2:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE')


    print('=' * 40)
jokenpo()

print('-=' * 13)

item = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print(f'''Computador jogou {item[computador]}
jogador jogou {item[jogador]}''')
print('-=' * 13)



if computador == 0 and jogador == 1:print(f'O jogador VENCEU! {item[jogador]} vence PEDRA')        
elif computador == 1 and jogador == 0:print(f'O computador VENCEU! {item[computador]} vence PEDRA')         
elif computador == 2 and jogador == 1:print(f'O computador VENCEU! {item[computador]} vence PAPEL')       
elif computador == 1 and jogador == 2:print(f'O jogador VENCEU! {item[jogador]} vence PAPEL')        
elif computador == 0 and jogador == 2:print(f'O computador VENCEU! {item[computador]} vence TESOURA')        
elif computador == 2 and jogador == 0:print(f'O jogador VENCEU! {item[jogador]} vence TESOURA')    
elif computador == jogador:print('EMPATE')
     
  