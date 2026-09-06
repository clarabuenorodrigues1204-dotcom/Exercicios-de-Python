from os import system
system('cls')

catalogo_livros = {}
lista_catalogo_livros = []

while True:
    
    catalogo_livros['Título'] = input('Título do livro: ').strip().title()
    catalogo_livros['Autor(a)'] = input('Autor(a): ').strip().capitalize()
    #Este bloco pede o número, verifica e valida se é ou não um número, se não for ele mostra mensagem pedindo que o usuário digite novamente
    ano = input('Ano de Publicação: ')
    while not ano.isdigit():
        ano = input('Digite APENAS números! Ano de Publicação: ') 
    
    catalogo_livros['Ano de Publicação'] = int(ano)    
      
    #Este bloco pede o número, verifica e valida se é ou não um número, se não for ele mostra mensagem pedindo que o usuário digite novamente   
    paginas = input('Nº de páginas: ')
    while not paginas.isdigit():
        paginas = input('Digite APENAS números! Nº de páginas: ')
        
    catalogo_livros['Nº de páginas'] = int(paginas)
       
    #Este bloco faz a verificação da data de publicação e decide qual será o status do livro
    if catalogo_livros['Ano de Publicação'] >= 2000:
        catalogo_livros['Status'] = 'Moderno'
        
    elif catalogo_livros['Ano de Publicação'] < 2000:
        catalogo_livros['Status'] = 'Antigo'
    #Este bloco verifica se o dicionário já recebeu 5 informações, se sim ele adiciona dentro da lista
    if len(catalogo_livros) == 5:
        lista_catalogo_livros.append(catalogo_livros.copy())
    #Pergunta ao usuário se ele quer continuar adicionando livros ao catálogo     
    escolha = str(input('Deseja continuar catalogando os livros? ')).strip().upper()
    #Valida se a escolha do usuário é 'S' - sim ou 'N' - não, se não for nenhuma das duas opção vai mostrar uma mensagem até o usuário digitar o correto
    while escolha != 'N' and escolha != 'S':
        escolha = str(input('Somente "S" ou "N". Deseja continuar catalogando os livros? ')).strip().upper()
    if escolha == 'S':
        continue
    elif escolha == 'N':
        break
#Parte responsável pela visualização das informações no terminal
print('╔' + '═' * 48 + '╗')
print('║' + 'CATÁLOGO DE LIVROS - LIVRARIA BUENOS'.center(48) + '║')
print('╠' + '═' * 48 + '╣')

for k, v in enumerate(lista_catalogo_livros, start=1):
    print('║' + f' LIVRO Nº {k} '.center(48, '─') + '║')

    print('║' + f' {"Título":<19} | {v["Título"]:<24}' +  '║')
    print('║' + f' {"Autor(a)":<19} | {v["Autor(a)"]:<24}' +  '║')
    print('║' + f' {"Ano de Publicação":<19} | {v["Ano de Publicação"]:<24}' +  '║')
    print('║' + f' {"Nº de páginas":<19} | {v["Nº de páginas"]:<24}' +  '║')
    print('║' + f' {"Status":<19} | {v["Status"]:<24}' +  '║')

    if k != len(lista_catalogo_livros):
        print('╠' + '═' * 48 + '╣')

print('╚' + '═' * 48 + '╝')