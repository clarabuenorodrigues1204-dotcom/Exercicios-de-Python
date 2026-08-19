from os import system
system('cls')
lista = [] #lista vazia
pessoas = []

for i in range(5):
    lista.append(int(input('Digite um número: '))) #Adiciona um elemento na lista a cada loop
    lista.sort(reverse=True) #ordena do maior pro menor
    
print(lista)

lista.insert(0, int(input('Digite mais um número: '))) #insere mais um elemento na lista (precisa indicar a posição desejada)
lista.sort(reverse=True) #ordena do maior pro menor

print(lista)
lista.remove(2)
lista.clear()#Ele simplesmente esvazia a lista, deixando ela [], mas a variável lista continua existindo e podendo ser usada depois


a = [2,3,4,5]
b = a[:] #Cria uma cópia dos valores da lista A, se eu fazer b = a vai criar uma ligação e quando eu quiser alterar um valor da lista, as duas listas vão ser alteradas
b[2] = 8
print(f'Lista A: {a}, Lista B: {b}')
pessoas.append(lista[:]) #Faz uma cópia de dados da primeira lista e adiciona essa cópia na lista pessoa. 