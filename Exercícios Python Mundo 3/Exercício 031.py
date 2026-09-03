from os import system
system('cls')

import sys

#funçao semelhante ao input
def leia(mensagem):
    print(mensagem, end="", flush=True)
    mensagem = sys.stdin.readline().strip() #Recebe o texto que o usuário digitou
    if not mensagem.isnumeric(): #Verifica se é um número, se não for número mostra mensagem de erro para: (-1,"aa"," ")
        print('ERRO! Digite um número inteiro válido.')    
    return mensagem #retorna o valor recebido


for i in range(3):
    n = leia('Digite um número: ')
    print(f'O {i + 1}º número digitado é {n}')
    print()