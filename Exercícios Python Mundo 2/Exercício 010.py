from os import system
system('cls')

print('{:=^40}'.format('LOJA BUENOs '))

preço_final = float(input('Qual é o valor final da compra? R$  '))
condição_do_pagamento = int(input('QUAL SERÁ A FORMA DE PAGAMENTO? \n 1 - PARA DINHEIRO \n 2 - PARA CHEQUE \n 3 - PARA PIX \n 4 - PARA CARTÃO \nQual é a opção: '))

desc_dinheiro = preço_final - (preço_final * 10 / 100)
desc_cartão = preço_final - (preço_final * 5 / 100)

if condição_do_pagamento == 1 or condição_do_pagamento == 2 or condição_do_pagamento == 3:
    print(f'O valor da sua compra com 10% de desconto ficará no total de: R${desc_dinheiro:.2f}')
    
if condição_do_pagamento == 4:   
    parcela = int(input('Em quantas parcelas você irá pagar? ')) 
    
    valor_parcela = preço_final / parcela 
    juros = (preço_final * 0.20) + preço_final
    final_cartão =  juros / parcela
    
    if parcela == 1:
        print(f'A sua compra com 5% de desconto ficará no total de: R${desc_cartão:.2f}')
    if parcela == 2:
        print(f'A sua compra ficará no total de R${preço_final:.2f}, e divido em {parcela:.2f}x sem juros, a suas parcelas ficaram no valor de: R${valor_parcela:.2f}')
    if parcela >= 3:
        print(f'O valor total da sua compra ficou em R${juros:.2f}, e divido em {parcela}x com 20% de juros, a suas parcelas ficaram no valor de: R${final_cartão:.2f}')
           



