from os import system
system('cls')

lista_numerica = []
cont = 1

while True:
    
    usuario = int(input(f'Digite o {cont}º valor: '))
    cont += 1
    
    if usuario not in lista_numerica: #Verifica se o valor que o usuário digitou não está na lista
        lista_numerica.append(usuario)
    
    if len(lista_numerica) == 6: #Verifica se a lista já atingiu o tamanho de 6 números digitados

        break    
    
lista_numerica = sorted(lista_numerica)   
print(f'Você digitos os valores {lista_numerica}')
    