from os import system
system('cls')

lista_pessoas = []
temp = []
pesos = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append( float(input('Peso(Kg): ')))
    
    if(len(lista_pessoas)) == 0: #Uma das maneiras de saber o maior e o menor número sem usar o max e min
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
            
        if temp[1] < menor:
            menor = temp[1]
            
    lista_pessoas.append(temp[:])
    temp.clear()
    
                  
    escolha = str(input('Quer continuar? ')).strip().upper()
        
    while escolha != 'N' and escolha != 'S':
        escolha = str(input('Quer continuar? ')).strip().upper()
        
    if escolha == 'S':
            continue
    elif escolha == 'N':           
        break           
        
print(f'Foram cadastradas o total de {len(lista_pessoas)} pessoas')
print(f'O maior peso foi de {maior}kg. Peso de:' , end='')

for p in lista_pessoas:
    if p[1] == maior:
            print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}kg. Peso de: ', end='')
for p in lista_pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')


