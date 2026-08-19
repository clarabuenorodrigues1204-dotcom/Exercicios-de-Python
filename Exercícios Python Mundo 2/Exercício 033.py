from os import system
system('cls')

print(f"{'=' * 40}\n{'PREÇOS BAIXOS':^40}\n{'=' * 40}")

counter_mil = sum_counter = menor_preço = 0
produto_barato = ' '

while True:
    
    nome_produto = str(input('Nome do produto: ')).strip().upper()
    preco_produto = float(input('Preço: R$'))
        
    sum_counter += preco_produto 
      
    if  preco_produto > 1000:
        counter_mil += 1
        
    if menor_preço == 0 or preco_produto < menor_preço:
        menor_preço = preco_produto
        produto_barato = nome_produto
           
    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()    
    
    if continuar != 'N' and continuar != 'S':
        print('Opção inválida! Tente novamente')      
        continue
    
    if continuar == "N":
        print(f"{'-' * 40}\n{'FIM DO PROGRAMA':^40}\n{'-' * 40}")
        break   
        
print(f'O total da compra foi de R${sum_counter:.2f}')       
print(f'Temos {counter_mil} produto na compra custando mais de R$ 1000.00')       
print(f'O produto mais barato foi {produto_barato} que custa R$ {menor_preço}') 
