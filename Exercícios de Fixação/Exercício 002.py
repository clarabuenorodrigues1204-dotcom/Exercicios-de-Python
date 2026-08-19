from os import system
system('cls')

#2. Maior e menor sem max() e min()
number = int(input(f'Digite o um número: '))
n = number
n2 = number

for i in range(1, 7):    
    number = int(input(f'Digite o um número: '))
    
    if number > n:
        n = number
    if number < n2:
        n2 = number
    
print(f'O maior número é: {n}')
print(f'O menor número é: {n2}')
    


        
    

        

