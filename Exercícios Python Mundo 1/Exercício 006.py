#Validador de senha
senha = input('Digite uma senha: ')
if len(senha) >= 8 and senha != '12345678':
    print('Senha valida')
elif len(senha) < 8:
    print('Senha invalida')
elif senha == '12345678':
    print('Senha óbvia demais')
        
        