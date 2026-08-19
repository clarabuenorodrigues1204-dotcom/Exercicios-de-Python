from os import system
system('cls')


print(f"{'=' * 40}\n{'BANCO CBR':^40}\n{'=' * 40}")

dinheiro = int(input('Qual valor você deseja sacar? '))
total = dinheiro
counter = 0
notas = 50

while True:
    if total >= notas:
        total -= notas
        counter += 1
          
    else:
        print(f'Total de {counter} notas de R${notas}')
            
        if notas ==50:            
            notas = 20
            
        elif notas == 20:
            notas = 10
            
        elif notas == 10:
            notas = 1
            
        counter = 0   
    
    if total == 0:
        if counter > 0:
            print(f'Total de {counter} notas de R${notas}')    
    
        break
