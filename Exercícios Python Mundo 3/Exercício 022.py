from os import system
system('cls')

ficha_temporaria = {}
lista_cidadoes = []
lista_mulheres = []
lista_idadesMaiores = []
count = sum_idades = 0

while True:
    
    ficha_temporaria['Nome'] = str(input('Nome: ')).strip().capitalize()
    ficha_temporaria['Gênero'] = str(input('Gênero: ')).strip().upper()
    
    while ficha_temporaria['Gênero'] != 'F' and ficha_temporaria['Gênero'] != 'M':
        
        print('OPÇÃO INVÁLIDA!')
        ficha_temporaria['Gênero'] = str(input('Gênero: ')).strip().upper()
        
    ficha_temporaria['Idade'] = int(input('Idade: '))
           
    if ficha_temporaria['Gênero'] == 'F':
        lista_mulheres.append(ficha_temporaria['Nome'])
    
    if len(ficha_temporaria) == 3:
        lista_cidadoes.append(ficha_temporaria.copy())
        count += 1
       
    
    escolha = str(input('Quer continuar [S/N]? ')).strip().upper()
        
    if escolha == 'S':
            continue
    elif escolha == 'N':
            break
        
    while escolha != "N" and escolha != "S":
        escolha = str(input('Quer continuar [S/N]? ')).strip().upper()

for k, v in enumerate(lista_cidadoes):
    sum_idades += v['Idade']

media = sum_idades / count

for k, v in enumerate(lista_cidadoes):    
    if v['Idade'] > media:
        lista_idadesMaiores.append((v['Nome'], v['Idade']))
        
print('=-'*40)
print(f'A) - Foram cadastradas {count} pessoas')
print(f'B) - A média de idade entre os cidadões é {media:.2f}')
print()
print('C) - LISTA DE MULHERES CADASTRADAS:')

for p, v in enumerate(lista_mulheres, start=1):
    print(f' {p}ª mulher cadastrada: {v}')
    
print()

print('D) - IDADES ACIMA DA MÉDIA:')    
for p, v in enumerate(lista_idadesMaiores, start=1):
    print(f' {p} - {v[0]} | idade: {v[1]}')