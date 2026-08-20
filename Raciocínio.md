Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:

 A) Quantas pessoas foram cadastradas.                                                                                                                
 B) Uma listagem com as pessoas mais pesadas.                                                                                                    
 C) Uma listagem com as pessoas mais leves.

1 - Criar uma lista vazia para ser armazenado os dados recebidos
2 - Criar a entrada do usuário e adicionar as informações recebidas na lista criada
3 - Fazer a verificação do peso a cada vez que o loop rodar e fazer um contador contando quantas pessoas foram cadastradas
    se a pessoa atual tiver o peso > que a pessoa anterior, faça -> enumerate
        inserir na lista de maior peso
    senão, faça
        adicionar na lista de menor peso
4 - mostrar na tela, o número de pessoas cadastradas e depois mostras os maiores pesos e os menores pesos.
    
---
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.

1- Criar uma lista que irá receber 7 números do usuário
2 - A cada volta do for verificar:
    se o número for par, faça:
        inserir na lista em tal posição
    senão, faça
        adicionar na lista
3 - mostrar na tela a lista ordenada em ordem crescente.

Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

1 - Criar uma lista que vai guardar 3 listas dentro dela e vão ser preenchidas de acordo com os números que o usuário digitar
2 - Entrada do usuário 
3 - Fazer um loop de 9 voltas, adicionar os números digitados dentro da primeira sublista.
    - se a primeira sublista atingir 3 números dentro dela, faça:
        adicionar os próximos números dentro da segunda sublista:
    - se a segunda sublista atingir 3 números, faça:
        adicionar os ultimos 3 números na terceira sublista