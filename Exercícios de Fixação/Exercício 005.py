from os import system
system('cls')

lista_valores = []


for i in range(1 , 8):
    lista = int(input(f'Digite o {i}º valor: '))
    
    for p, n in enumerate(lista_valores):     
                       
        if lista < n:
            lista_valores.insert(p, lista)
            break
                     
    else:
        lista_valores.append(lista)
        
    if lista_valores.count(lista) > 1:
        lista_valores.remove(lista)    
       
   
print(lista_valores)