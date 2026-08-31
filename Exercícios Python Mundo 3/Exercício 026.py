from os import system
system('cls')

from time import sleep

def maior(*num):
    tam = len(num)
    
    print('='*50)
    print('Analisando os valores passados...')   
    sleep(0.6)
    
    for valor in num:
        print(f'{valor}', end=' ',flush=True)   
          
    print(f'Foram informados {tam} números')
    print(f'O maior valor informado foi {max(num)}')
    
maior(1,3,5,6,8)
maior(3,5,9,1)
maior(2,6,1)
