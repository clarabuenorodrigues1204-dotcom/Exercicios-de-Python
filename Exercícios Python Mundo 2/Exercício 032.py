from os import system
system('cls')

counter = homens = mulheres = 0
while True:
    
    info_user = str(input('Informe seu sexo [M/F]: ')).upper().strip()
    
    if info_user != 'F' and info_user != 'M':
        print('Opção inválida! Tente novamente')
        continue
      
    idade = int(input('Qual é sua idade? '))
                  
    if idade > 18:
       counter += 1
       
    if info_user == "M":
       homens += 1
       
    if info_user == "F" and idade < 20:
        mulheres += 1
        
    print( "-" * 40)    
    user = str(input('Quer continuar [S/N]? ')).upper().strip()   
    print( "-" * 40)
    
    if user == "N":
        break
            
print(f'A {counter} pessoas maiores de 18 anos')     
print(f'Foram cadastrados {homens} homens ')
print(f'A {mulheres} mulheres menores de 20 anos cadastradas')
print( "-" * 40)
print("FIM DO PROGRAMA....")