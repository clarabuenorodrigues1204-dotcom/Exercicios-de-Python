from os import system
system('cls')

lista_matriz = [
    [],
    [],
    []
    ]
par = []
diag_p = []
pos = 0
somar = 0

for i in range(0, 9):
    num = int(input(f'Digite o {i}ª da matriz: '))
       
    lista_matriz[pos].append(num)
    
# Verificando se a primeira sublista atingiu 3 números, se sim, adiciona na segunda e se a segunda atingiu 3, vai pra terceira    
    if len(lista_matriz[pos]) == 3:
        pos += 1
        
# pegando os valores pares, colando em uma lista separada e depois somando eles   
    if num %2 == 0:  
        par.append(num)
        soma = sum(par)
       
# Extraindo a diagonal principal e somando os valores da terceira coluna
for p, linha in enumerate(lista_matriz):
    for v, elemento in enumerate(linha):
        if p == v:
            diag_p.append(lista_matriz[p][v])
        if v == 2:
            somar = somar + elemento
            
maior = max(lista_matriz[1])            

print('='*40)    
print(f'Sua Matriz 3x3 é:\n{lista_matriz[0]}\n{lista_matriz[1]}\n{lista_matriz[2]}')
print('='*40)
print(f'A diagonal principal é: {diag_p}')
print(f'A soma de todos os números pares da matriz é: {soma}')
print(f'A soma dos valores da terceira coluna é: {somar}')
print(f'O maior valor da segunda linha é: {maior}')
