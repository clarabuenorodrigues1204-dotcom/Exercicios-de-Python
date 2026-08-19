#FORMA QUE O MIRAI FEZ 
num = int(input('Quantos nomes serao digitados'))
listaDeAnimais = [] # [] ---> vazio

for i in range(num):
    animal = input('Nome do animal: ')
    listaDeAnimais.append(animal)

print(listaDeAnimais)