from os import system
system('cls')

#Testando os limites das funções "min()" e "max()"
lista_valor = []

for p in range(1, 6):
    lista_valor.append(int(input(f'Digite o {p}º valor: ')))
                
print(f'\nVocê digitou os valores {lista_valor}\n')

print(f'O maior valor digitado é {max(lista_valor) }, e se encontra nas posições: ', end='')

for i, v in enumerate(lista_valor):
    
    if v == max(lista_valor):
        print(f'{i}º', end=' ')
        

print(f'\nO menor valor digitado é {min(lista_valor) } e se encontra nas posições: ',end='')

for i, v in enumerate(lista_valor):
    if v == min(lista_valor):
        print(f'{i}º', end=' ')      
