from os import system
system('cls')

valor_casa = float(input('Digite o valor da casa que irá comprar: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Em quantos anos você pretende pagar a casa: '))

limite = salario * 0.30
parcela = valor_casa / (anos * 12)

if parcela > limite:
    print("Empréstimo negado!")
    
elif parcela <= limite:
    print("Empréstimo aprovado!")