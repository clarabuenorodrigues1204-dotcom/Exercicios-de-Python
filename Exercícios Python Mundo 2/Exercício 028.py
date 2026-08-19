from os import system
system('cls')

number = int(input('Digite um número: '))
choice = str(input('Quer continuar [S/N]: ')).upper().strip()
counter = 1
soma = number
maior = menor = number

while choice != "N":
    if choice != "S" and choice != "N":
        print('Opção inválida! Tente novamente')
        
    number = int(input('Digite um número: '))
    counter +=1
    soma += number
   
    
    if number > maior:
        maior = number
    
    if number < menor:
        menor = number
    
    choice = str(input('Quer continuar [S/N]: ')).upper().strip()
    
    
     
media = soma / counter
print(f'Você digitou {counter} números e a sua média foi {media:.2f}')

if maior == menor:
    print('Todos os números são iguais')
else:
    print(f'O maior valor foi {maior} e o menor valor foi {menor}')    


    