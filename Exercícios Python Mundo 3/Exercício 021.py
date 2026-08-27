from os import system
system('cls')


ficha_jogador = {}
total_gols = []

print(f'{'='*20} FICHA DOS JOGADORES {'='*20}')

while True:
    #Pede o nome e a quantidade de partidas jogadas e adiciona dentro de um dicionário
    ficha_jogador["name"] = str(input('Nome do jogador: ')).strip().capitalize()
    ficha_jogador["quant_partidas"] = int(input('Quantas partidas ele jogou? '))
    #Loop responsável por pegar a quantidade de partidas registradas e pergunta quantos gols foram feitos em cada partida, e depois adiciona em uma lista
    for i in range(ficha_jogador['quant_partidas']):
        gols_feitos = int(input(f'Quantos gols foram feitos na {i + 1}º partida: ')) 
        total_gols.append(gols_feitos)
     
    ficha_jogador["gols"] = total_gols   
    ficha_jogador["total de gols da temporada"] = sum(total_gols)#soma os gols e soloca no dicionário
    
    print(ficha_jogador)
    print()
    print(f'{'='*10}FICHA DO JOGADOR {ficha_jogador["name"]}{'='*10}')
    print(f'Nome do jogador: {ficha_jogador["name"]}\nPartidas jogadas: {ficha_jogador["quant_partidas"]}\nEle fez o total de {ficha_jogador["total de gols da temporada"]} gols na temporada')
    print(f'{'='*40}')
    escolha = str(input('Quer continuar [S/N]? ')).strip().upper()
    #Validação e verificação de escolha
    if escolha == 'S':
        continue
    elif escolha == 'N':
        break
    while escolha != "N" and escolha != "S":
        escolha = str(input('Quer continuar [S/N]? ')).strip().upper()