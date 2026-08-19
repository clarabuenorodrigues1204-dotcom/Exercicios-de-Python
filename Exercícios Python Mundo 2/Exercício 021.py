from os import system
system('cls')

info_user = str(input('Informe seu sexo [M/F]: ')).upper()

while info_user != "M" and info_user != "F":
    
    print('Dados inválidos. Tente novamente!')
    info_user = str(input('Informe seu sexo [M/F]: ')).upper()
    
if info_user == "M":
    print('Sexo masculino registrado com sucesso!')
    
elif info_user == "F":
    print('Sexo feminino registrado com sucesso!')