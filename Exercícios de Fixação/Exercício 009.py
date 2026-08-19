from os import system
system('cls')

from time import sleep


Lista_valores = []
while True:
    
    print(f'{'=-'*5} MENU INTERATIVO {'-='*5}')
    print("""[1] - Adicionar número
[2] - Remover número
[3] - Mostrar lista atual
[4] - Mostrar maior e menor
[5] - Sair do programa
""")
    
    escolha = int(input('Escolha uma opção: '))
    print('-'*37)
    
    if escolha == 1:
        
        number = int(input('Digite um valor para ser adicionado: '))
        Lista_valores.append(number)
        print(f'Número {number} adicionado com sucesso!')
    
    elif escolha == 2:
        remove = int(input('Qual número deseja remover: '))
        
        if remove not in Lista_valores:
            print('Este número não está na lista')
        else:
            Lista_valores.remove(remove)
            print('Número removido com sucesso!')

    elif escolha == 3:
        
        print(f'A lista atual é: {Lista_valores}')
    
    elif escolha == 4:
        
        if len(Lista_valores) == 0:
            print('A lista está vazia, adicione algo na lista.')
        else:
            print(f'O maior valor da lista é: {max(Lista_valores)}\nE o menor valor da lista é: {min(Lista_valores)}')
        
    elif escolha == 5:
        
        print('Saindo do programa...')
        sleep(1)
        print('FIM DO PROGRAMA!')
        break
        