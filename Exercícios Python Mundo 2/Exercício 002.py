from os import system
system('cls')

numero = int(input('Digite um número: '))
escolha = int(input('Escolha qual base de conversão você deseja: \n [1] - para binário \n [2] - para octal \n [3] - para hexadecimal \n Sua opção: ' ))

if escolha == 1:
  resultado = bin(numero)[2:]
  print(f'O seu número depois da conversão para BINÁRIO é: {resultado}')
  
elif escolha == 2:
    resultado = oct(numero)[2:] 
    print(f'O seu número depois da conversão para OCTAL é: {resultado}')
    
elif escolha == 3:
    resultado = hex(numero)[2:]
    print(f'O seu número depois da conversão HEXADECIMAL é: {resultado}')
else:
  print('OPÇÃO INVÁLIDA!')  

 
    

