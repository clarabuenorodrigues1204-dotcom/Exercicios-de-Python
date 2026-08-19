from os import system
system('cls')

lista_valores = [] #VAZIO
cont = 0
posicao = 1

while True:
    user_valores = int(input(f'Digite {posicao}º valor: '))
    posicao += 1
    lista_valores.append(user_valores)
    
    #Pergunta se o usuário quer continuar, e valida sua escolha
    user = str(input('Quer continuar? ')).strip().upper()    
    
    if user == "S":
        continue    
    
    elif user == "N":
        break
    
    elif user != "S" or user != "N":
        print('Digite uma opção válida!')
        user = str(input('Quer continuar? ')).strip().upper()    

#Verificando se o número 5 está dentro da lista       
if 5 in lista_valores:
        print('Número 5 está na lista')
else:
        print('O número 5 não foi encontrado na lista!')    
            
#Verificando quantas vezes o 5 apareceu na lista
for p, v in enumerate(lista_valores):  
        
    if v == 5:
        cont += 1
        
print(f'O número 5 apareceu {cont} vez(es)')
print(f'O 5 foi encontrado na posição {p}')
   

      
     
        

        
      
    
