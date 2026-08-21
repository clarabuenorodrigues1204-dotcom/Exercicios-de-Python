from os import system
system('cls')

from time import sleep

lista_notas = []
temp_notas = []
media = 0
escolha = 0

while True:
    #Menu da interface
    print(f'\n{'='*15} MENU DE NOTAS {'='*15}')
    print("""
[ 1 ] - Cadastrar notas dos alunos(a)
[ 2 ] - Mostrar notas de um aluno específico
[ 3 ] - Mostrar as notas de todos os alunos
[ 4 ] - Sair do programa 
        """)
    opcao = int(input('Qual é a opção desejada? '))
    #Validação do usuário na escolha da opção, NÃO pode ser maior que 4
    if opcao > 4:
        print(f'Digite uma opção válida!')
    #Funcionalidades da primeira opção    
    if opcao == 1:
        
        num = int(input('Quantos alunos deseja cadastrar? '))
        print()
        for i in range(num):
            #Coleta as informações e adiciona elas em uma lista temporária
            temp_notas.append (str(input('Nome do aluno(a): ')).strip().upper())
            temp_notas.append(float(input('Primeira nota: ')))
            temp_notas.append(float(input('Segunda nota: ')))
            #Faz a média das notas e adiciona na lista
            media = (temp_notas[1] + temp_notas[2]) / 2
            temp_notas.append(media)
            #Verifica se a lista temporária atingiu 4 informações adicionadas, se sim, adiciona na lista principal criando uma lista dentro de outra, e limpa a temporária
            if len(temp_notas) == 4:
                
                lista_notas.append(temp_notas[:])
                temp_notas.clear()
    #Funcionalidades da segunda opção           
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
    if opcao == 3:
        #Verifica se há alguma informação dentro da lista, se não houver algo na lista ele avisa, se não continua
        if len(lista_notas) == 0:
            print('Não há alunos cadastrados')
        else:
            #Mostra a lista de notas de todos os alunos cadastrados
            print(f'{'='*15}LISTA GERAL DE NOTAS{'='*15}\n')      
            for p , v in enumerate(lista_notas):
                print(f'{p + 1} - Nome: {v[0]} Nota1: {v[1]} Nota2: {v[2]} Média: {v[3]:.2f}')
        
    #Sai do programa   
    if opcao == 4:
        
        print('Saindo do programa...')
        sleep(1)
        break
        
    


   