from os import system
system('cls')

from time import sleep

def count(i,f,p):
    
    print(f'Contagem de {i} até o {f} pulando de {p} em {p} casas')
    
    
    for x in range(i,f,p):
        print(x, end=' ', flush=True)
        sleep(0.4)
              
    print()
    print('='*60)
    
count(1,11,1)
count(10,-1,-2)
print('Agora é sua vez de personalizar o contador!')
count(i = int(input('Inicio: ')) , f = int(input('Fim: ')), p = int(input('Passo[Somente positivo]: ')))