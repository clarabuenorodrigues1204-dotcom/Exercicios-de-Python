from os import system
system('cls')

from time import sleep

lista_notas = []
temp_notas = []
media = 0
escolha = 0
while True:
    print(f'{'=-'*8} MENU DE NOTAS {'-='*8}')
    print("""
[ 1 ] - Cadastrar notas dos alunos(a)
[ 2 ] - Mostrar notas de um aluno específico
[ 3 ] - Mostrar as notas de todos os alunos
[ 4 ] - Sair do programa 
        """)
    opcao = int(input('Qual é a opção desejada? '))
    if opcao > 4:
        print(f'Digite uma opção válida!')
        
    if opcao == 1:
        
        num = int(input('Quantos alunos deseja cadastrar? '))
        
        for i in range(num):
            
            temp_notas.append (str(input('Nome do aluno(a): ')).strip().upper())
            temp_notas.append(float(input('Primeira nota: ')))
            temp_notas.append(float(input('Segunda nota: ')))
            
            media = (temp_notas[1] + temp_notas[2]) / 2
            temp_notas.append(media)
            
            if len(temp_notas) == 4:
                lista_notas.append(temp_notas[:])
                temp_notas.clear()
                
    if opcao == 2:
        if len(lista_notas) == 0:
            print('Não há alunos cadastrados')
        else:
            print(f'{'=-'*5}Alunos cadastrados {'-='*5}')
        
            for p , v in enumerate(lista_notas):
                print(f'{p + 1} - {v[0]}') 
            
            escolha = int(input('Qual aluno(a) deseja ver o boletim? '))
        
            if escolha < 1 or escolha > len(lista_notas):
                print('Escolha uma opção válida')                     
            else:
                for p , a in enumerate(lista_notas):
                    if escolha - 1 == p:
                        print(f"""{'=-'*4}BOLETIM ESCOLAR{'-='*4} \nALUNO(A): {a[0]}\nNota 1: {a[1]}\nNota 2: {a[2]}\nMédia: {a[3]}""")
                    
    if opcao == 3:
        if len(lista_notas) == 0:
            print('Não há alunos cadastrados')
        else:
            
            print(f'{'=-'*5}LISTA GERAL DE NOTAS{'-='*5}\n')      
            for p , v in enumerate(lista_notas):
                print(f'{p + 1} - Nome: {v[0]}, Nota1: {v[1]}, Nota2: {v[2]}, Média: {v[3]}')
        
        
    if opcao == 4:
        print('Saindo do programa...')
        sleep(1)
        break
        
    


   