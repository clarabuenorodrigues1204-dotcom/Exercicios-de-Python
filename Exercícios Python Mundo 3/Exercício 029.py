from os import system
system('cls')

n = int(input('Digite o número que será fatorado: '))

def fatorial(n,show = False):
    fat = 1    
    if n <= 1:
        return 1
    else:
        
        for i in range(n, 0, -1):
            if show:
                print(i,end='')
                      
                if i != 1:
                    print(end=' x ')
                else:           
                    print(f' = {fatorial(n)}')  
                
            fat *= i         
    return fat
print(f'O resultado do cálculo {n} fatorial é: ', end=' ')
fatorial(n , show=True)
