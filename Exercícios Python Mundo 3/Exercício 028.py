from os import system
system('cls')


ano_nascimento = int(input('Ano de nascimento: '))

def voto(ano_nascimento):
    
    from datetime import date
    idade = date.today().year - ano_nascimento
            
    if  idade >= 16 and idade <= 17 or idade >= 65:
        print(f'Você tem {idade} anos de idade. Status: VOTO OPCIONAL')
    
    elif idade >= 18:
        print(f'Você tem {idade} anos de idade. Status: VOTO OBRIGATÓRIO')
              
    elif idade < 16:
        print(f'Você tem {idade} anos de idade. Status: NÃO VOTA')

voto(ano_nascimento)
