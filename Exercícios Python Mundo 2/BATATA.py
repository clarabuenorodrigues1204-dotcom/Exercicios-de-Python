from os import system
from time import sleep
system('cls')

#Versão feita pelo mirai


def header():
    system('cls')
    print("=========== BUENO'S STORE ===========\n")

def loadSimulation():
    print('Loading')

    for _ in range(3):
        print('.', end="", flush=True)
        sleep(0.4)

    print('\n')

header()
loadSimulation()

valor = float(input("Qual é o valor final da compra? R$ "))

print("\nQual será o meio de pagamento?")
print("1 - PARA DINHEIRO")
print("2 - PARA CHEQUE")
print("3 - PARA PIX")
print("4 - PARA CARTÃO")

for i in range(2):
    loadSimulation()

opcao = int(input("A opção escolhida é: "))

if opcao == 1:
    header()
    desconto = valor * 0.10
    total = valor - desconto

    print("O valor total da sua compra ficou em R${:.2f} com 10% de desconto.".format(total))

if opcao == 2:
    header()
    desconto = valor * 0.05
    total = valor - desconto

    print("O valor total da sua compra ficou em R${:.2f} com 5% de desconto.".format(total))

if opcao == 3:
    header()
    desconto = valor * 0.15
    total = valor - desconto

    print("O valor total da sua compra ficou em R${:.2f} com 15% de desconto.".format(total))

if opcao == 4:
    header()
    parcelas = int(input("Em quantas parcelas você irá pagar? "))

    if parcelas <= 3:
        total = valor
        parcela = total / parcelas

        print("O valor total da sua compra ficou em R${:.2f}, dividido em {}x sem juros, as parcelas ficaram no valor de R${:.2f}".format(total, parcelas, parcela))

    if parcelas >= 3:
        juros = valor * 0.20
        total = valor + juros
        parcela = total / parcelas

        print("O valor total da sua compra ficou em R${:.2f}, dividido em {}x com 20% de juros, as suas parcelas ficaram no valor de R${:.2f}".format(total, parcelas, parcela))


print("Finalizando")
loadSimulation()   