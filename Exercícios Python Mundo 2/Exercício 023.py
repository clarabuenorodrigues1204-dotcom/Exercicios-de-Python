from os import system
system('cls')

primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
escolha = 0

while escolha != 5:
    print('-=' * 15)
    print("""Interface               
[1] - Somar
[2] - Multiplicar 
[3] - Maior
[4] - Novos números
[5] - Sair do programa\n""")
    
    escolha = int(input('Qual opção você escolhe:')) 
    print('-=' * 15)  
       
    if escolha == 1:
        soma = primeiro_valor + segundo_valor
        print(f'A soma entre {primeiro_valor} e {segundo_valor} é: {soma}')
        
    elif escolha == 2:
        multiplicacao = primeiro_valor * segundo_valor
        print(f'O resuldado da multiplicação entre {primeiro_valor} e {segundo_valor} é: {multiplicacao}')
        
    elif escolha == 3:
        if primeiro_valor  > segundo_valor:
            print(f'Entre {primeiro_valor} e {segundo_valor}, o maior valor é {primeiro_valor} ')
            
        elif segundo_valor > primeiro_valor:
            print(f'Entre {primeiro_valor} e {segundo_valor}, o maior é {segundo_valor}')
            
        else:
            print('Os dois valores são iguais')
            
    elif escolha == 4:
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))
        
    elif escolha == 5:
        print('Saindo do programa...')
        
    else:
        print('Opção inválida! Tente novamente')
        
print("Fim do programa! Volte sempre")
 