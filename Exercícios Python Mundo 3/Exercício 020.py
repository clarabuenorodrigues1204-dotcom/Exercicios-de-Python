from os import system
system('cls')
from datetime import datetime

ficha_cidadao = {}
fichas_cidadoes = []
idade_aposentadoria = 65 #idade supositória 

print(f"""
{'=' * 50}
          INSIRA OS DADOS DO CIDADÃO
{'=' * 50}
""")
 
 
while True:                    
    #Adiciona no dicionário as informações essenciais
    ficha_cidadao["Nome"] = str(input('Nome: ')).strip().capitalize()

    ficha_cidadao["Ano de Nascimento"] = int(input('Ano de nascimento: '))
    #Cálculo da idade usando ano atual  - idade digitada
    ficha_cidadao["Idade"] = datetime.now().year - ficha_cidadao['Ano de Nascimento']
    #Interface de verificação para saber se o cidadao tem ou não CTPS
    print(f"""{'='*7} ESSE CIDADÃO POSSUI CTPS DIGITAL? {'='*7}
[ 0 ] - Não
[ 1 ] - Sim
    """)
    ctps = int(input('Escolha uma opção: '))
    #Se tiver CTPS, Vão ser adicionados esses dados a ficha do cidadao
    if ctps == 1:
        
        print('='*50)
        ficha_cidadao["Nº CTPS digital"] = str(input('Nº Da CTPS Digital: '))
        
        ficha_cidadao["Ano de contratação"] = int(input('Ano de contratação: '))
        
        ficha_cidadao["Salário"] = float(input('Salário: '))   
        
        ficha_cidadao["Anos Faltantes para a aposentadoria"] = idade_aposentadoria -  ficha_cidadao["Idade"]
        
        fichas_cidadoes.append(ficha_cidadao.copy())
        #Se a opção for "sim" mostra ficha completa, se não, começa um novo cadastro
        print(f"""{'='*3} DESEJA MOSTRAR A FICHA COMPLETA DO CIDADÃO? {'='*3}
              
[1] - SIM
[2] - NÃO
""")
        opcao = int(input("Escolha uma opção: "))
        
        
        if opcao == 1:    
            for k, v in enumerate(fichas_cidadoes):
                print(f"""
        {'=' * 45}
                    FICHA COMPLETA DO(A) CIDADÃO #{k + 1}
        {'=' * 45}
        |Nome: {v["Nome"]}
        |Ano de nascimento: {v["Ano de Nascimento"]}
        |Idade: {v["Idade"]} anos
        |Nº CTPS Digital: {v["Nº CTPS digital"]}
        |Ano de contratação: {v["Ano de contratação"]}
        |Salário: R$ {v["Salário"]:.2f}
        |Anos faltantes para aposentadoria: {v["Anos Faltantes para a aposentadoria"]} anos
        {'=' * 45}
        """)
            break
            
        elif opcao == 2:
            print(f"""
{'=' * 50}
          INSIRA OS DADOS DO CIDADÃO
{'=' * 50}
""")
            continue
        
    elif ctps == 0:
        
        print(f"""
{'=' * 50}
|            FICHA ATUAL DO(A) CIDADÃO           |
{'=' * 50}
| Nome: {ficha_cidadao["Nome"]}                                             
| Ano de Nascimento: {ficha_cidadao["Ano de Nascimento"]}                       
| Idade: {ficha_cidadao["Idade"]} anos                                      
{'=' * 50}
""")
        break


