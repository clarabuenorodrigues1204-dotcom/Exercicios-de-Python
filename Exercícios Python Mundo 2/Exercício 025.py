from os import system
system('cls')

#Progração Aritmética v2 e v3

primeiro_termo = int(input('Digite o 1° termo: '))
razao = int(input('Digite a razão: '))
c = primeiro_termo
contador = 1
total = 0
mais = 10
print(f'{primeiro_termo}' , end = ' → ')

while mais != 0:
    total = total + mais       
    while contador <= total:
        print(f'{c}', end= ' → '  )
        c += razao
        contador += 1
    print("PAUSA")
    mais = int(input('\nQuantos termos a mais você quer mostrar? '))
