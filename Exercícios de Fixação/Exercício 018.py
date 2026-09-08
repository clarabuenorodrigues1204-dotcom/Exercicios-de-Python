from os import system
system('cls')

catalogo_jogos = {}
lista_catalogo_jogos = []
notas = []
media = soma = cont = 0

while True:
    catalogo_jogos['Nome'] = input('Nome do jogo: ').strip().title()
    catalogo_jogos['Gênero'] = (input('Gênero do jogo: ')).strip().upper()       
     
    #Pega a nota que está no tipo 'string' e converte para 'float'
    nota = input('Nota do jogo [0 a 10]? ')
    nota = float(nota)
    
    #Verifica e valida se a nota recebida foi menor que 0 ou maior que 10, se sim mostra mensagem
    while nota < 0 or nota > 10:
        nota = input('Digite uma nota de 0 a 10: ')
        
        while not nota.replace('.', '', 1).isdigit():
            nota = input('Digite um número válido [0 a 10]: ')
            
        nota = float(nota)       
    #Depois da verificação e conversão, adiciona a nota no dicionário
    catalogo_jogos['Nota'] = nota
    
    #Verifica se o dicionário atingiu 3 informações, se sim, adiciona lista  
    if len(catalogo_jogos) == 3:
        
        lista_catalogo_jogos.append(catalogo_jogos.copy())
        print(lista_catalogo_jogos)
    
    escolha_usuario = input('Deseja continuar catalogando os jogos? ').strip().upper()
    
    #Validação e verificação da escolha do usuário
    while escolha_usuario != 'S' and escolha_usuario != 'N':
        
        escolha_usuario = input('Opção inválida! Digite apenas [S/N]. Deseja continuar? ').strip().upper()
    
    if escolha_usuario == 'S':
        continue
    elif escolha_usuario == 'N':
        print('FIM DO PROGRAMA...')
        break
    
#Percorre a lista de dicionários e soma as notas   
for notas_jogo in lista_catalogo_jogos:
    soma += notas_jogo['Nota']
    
#Faz a média das notas    
media = soma / len(lista_catalogo_jogos)

#Verifica se as notas dos jogos é maior que a média das notas, se sim, adiciona no contador
for notas_media in lista_catalogo_jogos:
    if notas_media['Nota'] > media:
        cont += 1
        
#Adiciona somente as notas em uma lista separada, depois pega a maior e a menor nota     
for nota in lista_catalogo_jogos:
    notas.append(nota['Nota'])
    
maior = max(notas)
menor = min(notas) 

print('╔' + '═' * 48 + '╗')
print('║' + 'CATÁLOGO DE JOGOS- LAN HOUSE BUENOS'.center(48) + '║')
print('╠' + '═' * 48 + '╣')

for k, v in enumerate(lista_catalogo_jogos, start=1):
    print('|' + f'JOGO Nº {k}'.center(48) + '|')
    print('|' + '-'*48 + '|')
    print('|' + f' {"Nome":<19} | {v["Nome"]:<24}' +  '|')
    print('|' + f' {"Gênero":<19} | {v["Gênero"]:<24}' +  '|')
    print('|' + f' {"Nota":<19} | {v["Nota"]:<24}' +  '|')
    print('-'*48)
    
print('-'+ f'{"="*18}Dados Gerais{"="*18}')   
print('-'+ f' A maior nota foi {maior} | e a menor nota foi {menor}')
print('-'+ f' A média de notas dos jogos é {media:.2f}')
print('-'+ f' Há {cont} jogo(s) acima da média')


    
    