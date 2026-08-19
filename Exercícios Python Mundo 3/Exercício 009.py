from os import system
system('cls')

lista_n = []

for i in range(0, 5):
    lista = int(input('Digite um valor: '))
    
    
    for p, n in enumerate(lista_n):
        
        if lista < n:
            lista_n.insert(p, lista)
            print(f'Adicionado na posição {p} lista')
            break
    else: 
        print(f'Adicionado na posição {len(lista_n)} da lista')            
        lista_n.append(lista)
        
print(lista_n)
    
      

 