from os import system
system('cls')


info_pessoas = []

soma_idades = 0
maior_idade = 0
nome_maisVelho = 0
mulher_idade = 0

for p in range(1, 5):
    pessoas = []
    
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Idade: ')))
    pessoas.append(str(input('Sexo [M/F]: ')))
    
    info_pessoas.append(pessoas)
    
for i in range(len(info_pessoas)):
    
    soma_idades += info_pessoas[i][1]    

media = soma_idades / len(info_pessoas)


for h in range(len(info_pessoas)):
    if info_pessoas[h][2] == "M":
        if info_pessoas[h][1] > maior_idade:
            maior_idade = info_pessoas[h][1]
            nome_maisVelho = info_pessoas[h][0]
            
for m in range(len(info_pessoas)):
    if info_pessoas[m][2] == "F":
        if info_pessoas[m][1] < 20:
           mulher_idade += 1
        
        

print(f'A media d a idade do grupo é de {media}')
print(f'O Nome do homem mais velho é {nome_maisVelho}')
print(f' A {mulher_idade} mulherers menores de 20 anos')