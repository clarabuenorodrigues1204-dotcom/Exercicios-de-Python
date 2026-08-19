from os import system
system('cls')


#Tabuada v3

while True:
    n = int(input('Você gostaria de ver a tabuada de qual valor? '))
    
    print("-" * 40)
    
    if n < 0:
        print('FIM DO PROGRAMA! VOLTE SEMPRE')
        break
    
    for m in range(1, 11):
        print(f'{n} x {m} = {n * m}')
        
    print("-" * 40)
    