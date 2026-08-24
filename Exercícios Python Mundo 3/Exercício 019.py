from os import system
system('cls')

from random import randint
from time import sleep

dados_jogados = {}
resultado_ordenado = []

print(f'{'='*10}ROLAGEM DE DADOS{'='*10}')

for jogadores in range(0,4):
    
    dados_jogados['Nome'] = str(input(f'Nome do {jogadores + 1}º jogador(a): ')).capitalize().strip()
    dados_jogados['result_dados'] = randint(1, 6)
    resultado_ordenado.append(dados_jogados.copy())
    
for p, v in enumerate(resultado_ordenado):
   resultado_ordenado = sorted(resultado_ordenado, key=lambda v: v['result_dados'])

resultado_ordenado = sorted(resultado_ordenado,key=lambda v: v['result_dados'],reverse=True)
print(f'{"=" * 10} RESULTADO DAS JOGADAS {"=" * 10}')

for pos, jogador in enumerate(resultado_ordenado, start=1):
    print(f'{pos}º lugar → {jogador["Nome"]:<15} 🎲 {jogador["result_dados"]}')
    sleep(0.8)
print('=' * 44)

