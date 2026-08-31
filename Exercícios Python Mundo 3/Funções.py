from os import system
system('cls')

#Sem parâmetro
def dados():  
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        print(nome,idade)
dados()

#Com parâmetro
def nomes(name):
    print(f'Olá {name}')
#não precisa indicar o tipo da váriavel, quando o parâmetro receber o argumento o python saberá o tipo sozinho    
name = input('Nome: ') 
nomes(name)

#empacotamento e desempacotamento
lista = []
def pac (*num): #empacotamento
    tam = len(lista)
    print(num,tam)
for i in range(0,5):
    num = input('Numeros :')
    lista.append(num)
pac(*lista) # - desempacotamento

#parâmetro opcional
def somar (a=0,b=0,c=0):
    s = a + b + c
    print(s)
somar(2,5,6)
somar(2,5,)
somar(2)