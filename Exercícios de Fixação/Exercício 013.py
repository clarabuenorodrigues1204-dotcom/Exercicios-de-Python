from os import system
system('cls')

lista_cadastro = []


while True:
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
   
    for p, v in enumerate(lista_cadastro):
        if idade < v[1]:
            lista_cadastro.insert(p, (nome , idade))
            break
    else:
        len(lista_cadastro)
        lista_cadastro.append((nome , idade))
            
    escolha = str(input('Quer continuar? ')).strip().upper()
    
    while escolha != 'N' and escolha != 'S':
        escolha = str(input('Quer continuar? ')).strip().upper()
    if escolha == 'S':
        continue
    elif escolha == 'N':
        break
    
    
print(lista_cadastro)
