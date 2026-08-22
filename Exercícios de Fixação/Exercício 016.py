from os import system
system('cls')

from time import sleep

lista_notas = []
temp_notas = []
lista_aprovados = []
lista_reprovados = []
media = 0
escolha = 0

while True:
    #Menu da interface
    print('+' + '=' * 43 + '+')
    print('|{:^43}|'.format('MENU DE NOTAS'))
    print('+' + '=' * 43 + '+')
    print('| {:<41}|'.format('[ 1 ] - Cadastrar alunos'))
    print('| {:<41}|'.format('[ 2 ] - Mostrar boletim de um aluno'))
    print('| {:<41}|'.format('[ 3 ] - Mostrar todos os alunos'))
    print('| {:<41}|'.format('[ 4 ] - Mostrar aprovados'))
    print('| {:<41}|'.format('[ 5 ] - Mostrar reprovados'))
    print('| {:<41}|'.format('[ 6 ] - Sair'))
    print('+' + '=' * 43 + '+')
    opcao = int(input('Qual é a opção desejada? '))
    #Validação do usuário na escolha da opção, NÃO pode ser maior que 
    if opcao > 6:
        print(f'Digite uma opção válida!')
    #Funcionalidades da opção 1  
    if opcao == 1:
        
        num = int(input('Quantos alunos deseja cadastrar? '))
        print()
        
        for i in range(num):
            #Coleta as informações e adiciona elas em uma lista temporária
            print('╔' + '═' * 42 + '╗')
            print(f'║{f" FICHA DO(A) {i + 1}º ALUNO(A) ":^42}║')
            print('╠' + '═' * 42 + '╣')

            temp_notas.append(str(input('║ Nome do aluno(a): ')).strip().upper())
            temp_notas.append(float(input('║ Primeira nota: ')))
            temp_notas.append(float(input('║ Segunda nota: ')))

            print('╚' + '═' * 42 + '╝')
            print()
            #Faz a média das notas e adiciona na lista
            media = (temp_notas[1] + temp_notas[2]) / 2
            temp_notas.append(media)
            #Verifica se a lista temporária atingiu 4 informações adicionadas, se sim, adiciona na lista principal criando uma lista dentro de outra, e limpa a temporária
            if len(temp_notas) == 4:
                
                lista_notas.append(temp_notas[:])
                temp_notas.clear()
    #Funcionalidades da opção 2           
    if opcao == 2:
        #Verifica se há alguma informação dentro da lista, se não houver algo na lista ele avisa, se não continua
        if len(lista_notas) == 0:
            print('Não há alunos cadastrados')
        else:
            print(f'{'='*12} ALUNOS CADASTRADOS {'='*12}')
            #Númera a lista e mostra os alunos cadastrados
            for p , v in enumerate(lista_notas):
                print(f'{p + 1} - {v[0]}') 
            print(f'{'='*44}')
            
            escolha = int(input('Qual aluno(a) deseja ver o boletim? '))
            #Se o usuário escolheu uma opção inexistente, o programa avisa, se não ele continua e mostra o boletim do aluno escolhido
            if escolha < 1 or escolha > len(lista_notas):
                print('Escolha uma opção válida')                     
            else:
                for p , a in enumerate(lista_notas):
                    if escolha - 1 == p:
                        print(f"""\n{'='*8}BOLETIM ESCOLAR{'='*8} \nALUNO(A): {a[0]}\nNota 1: {a[1]}\nNota 2: {a[2]}\nMédia: {a[3]}""")
                        print(f'{'='*31}')
    #Funcionalidades da opção 3
    if opcao == 3:
        #Verifica se há alguma informação dentro da lista, se não houver algo na lista ele avisa, se não continua
        if len(lista_notas) == 0:
            print('Não há alunos cadastrados')
        else:
            #Mostra a lista de notas de todos os alunos cadastrados
            print(f'{'='*15}LISTA GERAL DE NOTAS{'='*15}\n')      
            for p , v in enumerate(lista_notas):
                print(f'{p + 1} - Nome: {v[0]} Nota1: {v[1]} Nota2: {v[2]} Média: {v[3]:.2f}')
    #Funcionalidades de opção 4
    if opcao == 4:  
        
        print(f'{'='*12}LISTA DOS APROVADOS{'='*12}\n')     
        #Verifica se algum aluno cadastrado tem a média >= 6, se sim, adiciona em outra lista (lista_aprovados)
        for i , a in enumerate(lista_notas):
            if a[3] >= 6:  
                lista_aprovados.append((a[0] , a[3]))
                
        lista_aprovados = sorted(lista_aprovados, key=lambda a: a[1], reverse=True)        
        #Verifica se há algum aprovado na lista, se não tiver, exibe uma mensagem
        if len(lista_aprovados) == 0:
            print('Não há alunos aprovados!')        
        else:
        #Mostra a lista de aprovados, que está ordenado de forma decrescente e depois de exibido apaga a (lista de aprovados)
            for p, a in enumerate(lista_aprovados):
                print(f'{p + 1}º - Nome: {a[0]} | Média: {a[1]:.2f}')
            
        lista_aprovados.clear()
    #Funcionalidades da opção 5       
    if opcao == 5:
        print(f'{'='*12}LISTA DOS APROVADOS{'='*12}\n')
        #Verifica se algum aluno cadastrado tem a média < 6, se sim, adiciona em outra lista (lista_reprovados)
        for i , a in enumerate(lista_notas):
            if a[3] < 6:  
                lista_reprovados.append((a[0], a[3]))
                
        lista_reprovados = sorted(lista_reprovados, key=lambda a: a[1])
        
        if len(lista_reprovados) == 0:
                    print('Não há alunos reprovados!')  
        else:
        #Mostra a lista de reprovados, que está ordenada de forma crescente e depois de exibido apaga a (lista_reprovados)
            for p, a in enumerate(lista_reprovados):
                print(f'{p + 1}º - Nome: {a[0]} | Média: {a[1]:.2f}')
            
        lista_reprovados.clear()
    #Sai do programa   
    if opcao == 6:
        
        print('Saindo do programa...')
        sleep(1)
        break
        
    


   