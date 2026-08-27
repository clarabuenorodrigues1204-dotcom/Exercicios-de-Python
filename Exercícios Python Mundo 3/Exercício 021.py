from os import system
system('cls')


ficha_jogador = {}
ficha_jogadores = []
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
        
    ficha_jogador['Gols'] = total_gols[:]   
    ficha_jogador["total de gols da temporada"] = sum(total_gols)#soma os gols e soloca no dicionário
    total_gols.clear()
    
    ficha_jogadores.append(ficha_jogador.copy())
    escolha = str(input('Quer continuar [S/N]? ')).strip().upper()
    print('='*71)
    #Validação e verificação de escolha
    if escolha == 'S':
        continue
    elif escolha == 'N':
        break
    while escolha != "N" and escolha != "S":
        escolha = str(input('Quer continuar [S/N]? ')).strip().upper()
    
print()
print(f'{'='*25} FICHA DOS JOGADORES {'='*25}')

for k, v in enumerate(ficha_jogadores,start=1):
    print(f'{k} - Nome: {v["name"]} | Partidas: {v["quant_partidas"]} | GOLS: {v["Gols"]} TOTAL DE GOLS: {v["total de gols da temporada"]}')
print(f'{'='*71}')

#Responsável por mostrar a ficha do jogador escolhido
while True:
    
    escolha = int(input('Mostrar dados de qual jogador? '))
    print()
    #Verifica se a escolha do usuário existe dentro da lista, se não estiver na lista avisa, senão, se estiver ele mostra a ficha escolhida
    if escolha > len(ficha_jogadores):
        print('ERRO! Não existe esse jogador na lista')
    else:
        for k, v in enumerate(ficha_jogadores):
            if escolha - 1 == k:
                print(f'{'='*10}Ficha do jogador {v["name"]}{'='*10}')
                print(f'Nome: {v["name"]}\nPartidas jogadas: {v["quant_partidas"]}\nGols: {v["Gols"]}\nGols totais: {v["total de gols da temporada"]}')
                
    print('='*45)
    
    parada = str(input('Deseja encerrar o programa? ')).strip().upper()
    #Validação de parada
    while parada != "N" and parada != "S":
        parada = str(input('OPÇÃO INVÁLIDA! DIGITE S OU N: ')).strip().upper()
    if parada == 'N':
        continue
    elif parada == 'S':
        break