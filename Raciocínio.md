## 6. Remoção controlada

Crie uma lista de números.

Depois peça um número ao usuário:

- Se ele existir, remova a primeira ocorrência;
- Se não existir, informe isso.

**Foco:** diferença entre `remove()` e `pop()`.


1- Criar uma lista pré - definida
2 - entrada do usuário 
3 - validar a entrada do usuário
Se a entrada do usuário estiver dentro da lista
- remover
Se a entrada do usuário não estiver dentro da lista
- avisar que ela não existe dentro da lista

---
## 7. Removendo repetidos

Receba uma lista que pode possuir números repetidos.

Crie uma segunda lista contendo cada número apenas uma vez.

**Não utilize `set()`**.

**Foco:** `in`, `append()` e criação de novas listas.

1 - Criar uma lista vazia que será preenchida pelo usuário
2-  Receber entrada do usuário a cada loop
3 - adicionar esses números na lista
4 - se este número já estiver dentro da primeira lista adicionar em uma segunda lista
5 - mostrar segunda lista sem os números repetidos

---
## 8. Seis números diferentes

O usuário deve fornecer **6 números diferentes**.

Se digitar um número repetido:

- Não contabilize;
- Peça outro número.

No final, mostre os seis números em ordem crescente.

**Foco:** `while True`, `break`, `len()` e `in`.

1 - Criar uma lista vazia e ir preenchendo de acordo com o que o usuário digita.
2 -  Pedir um número para o usuário 6 números diferentes.
3 - Enquanto for verdade faça:
- se o número não estiver dentro da lista adicione.
- senão, se o número já estiver dentro da lista, peça outro número.
4 - se o tamanho da lista for igual a 6, pare!

---
## 9. Menu de operações

Crie um programa que continue funcionando até o usuário escolher sair.

O menu deve permitir:

1. Adicionar número;
2. Remover número;
3. Mostrar lista;
4. Mostrar maior e menor;
5. Sair.

**Foco:** `while`, condicionais e manipulação de listas.

1 - Criar uma lista vazia 
2 - Criar um menu interativo com 5 opções
3 - Criar a entrada do usuário
4 - Criar funções e executa - lás de acordo com a escolha do usuário

- Adicionar número
	- Se o usuário escolheu a opção 1, faça:
	 usuário digita o número que quer adicionar
		número é adicionado imediatamente na lista

- Remove o número
	- Senão, se usuário escolher a opção 2, faça:
		usuário informa qual número quer remover da lista
			programa percorre a lista, encontra o número e remove
			
- Mostra a lista
	- Senão, se o usuário escolher a opção 3, faça:
		mostra a lista atual na tela para o usuário

- Mostra o maior e menor número
	- Senão, se o usuário escolher a opção 5, faça:
		mostra o maior e o menor número da lista atual

- Saída
	- Senão, se o usuário escolher a opção 6, faça:
		se a escolha  for igual a 6
			pare o programa.
		

---
## 10. Par, ímpar e geral

Leia números até o usuário decidir parar.

Mantenha três listas:

- Lista geral;
- Lista de pares;
- Lista de ímpares.

No final, mostre as três listas.

**Foco:** diferenciar o valor atual da lista inteira.

1 - Criar 3 listas
- Lista geral
- Lista de números pares
- Lista de números ímpares
2 - Criar a entrada do usuário
3 - adicionar o número digitado pelo usuário dentro da lista geral
4 - Se o número digitado for par, faça:
	adicione na lista de números pares
Se não, faça:
	adicione na lista de números ímpares

5 - Fazer estrutura de validação para a escolha do usuário em relação a continuar com o programa
 - enquanto a escolha for diferente de sim ou não, faça:
	 repetir a pergunta até ser s ou n
- se escolha for igual a sim, faça:
	- continue
- senão, se for igual a não, faça:
	- pare
6 - Mostrar na tela as 3 listas.

---

## 11. Análise de uma tupla

Crie uma tupla contendo 10 números.

Informe:

- Maior valor;
- Menor valor;
- Quantidade de determinado valor;
- Posições em que determinado valor aparece.

**Foco:** índices, `count()`, `enumerate()` e `in`.

1 - Criar uma tupla definida com 10 números
2- Criar uma lista para guardas as posições desejadas
3 - pegar o maior e o menor valor da tupla
4 - usuário informa qual valor ele deseja saber: 
	 - verificar quantas vezes determinado valor apareceu
	 - verificar em qual posição aquele valor apareceu
5 - mostrar na tela maior valor, menor valor, quantidade de determinado valor e posição de determinado valor

---

## 12. Lista de preços

Crie uma lista contendo produtos e seus respectivos preços.

Depois mostre:

- Todos os produtos;
- Produto mais caro;
- Produto mais barato;
- Valor total.

**Foco:** estruturas aninhadas e acesso aos elementos.


1 - Criar uma lista com o nome e o preço do produto
2 - Mostrar lista completa
3 - Mostrar o produto mais caro
	acessar o produto mais caro através dos índices da segunda fileira
4 - Mostrar o produto mais barato
	acessar o produto mais caro através dos índices da segunda fileira
5 - somar o valor de todos os produtos

---
## 13. Cadastro ordenado

Crie um cadastro contendo:

- Nome;
- Idade.

As pessoas devem ser inseridas mantendo a lista ordenada pela idade.

**Foco:** `insert()`, `enumerate()` e comparação.

1 - Criar uma lista vazia que irá receber o nome e a idade
2 - criar duas entradas de usuário, uma chamada nome e outra idade
3 - Adicionar a primeiro nome + idade dentro da lista
4 - Percorrer as pessoas já cadastradas e comparar a idade da nova pessoa com a idade de cada pessoa. Quando encontrar uma idade maior que a nova idade, inserir a nova pessoa naquela posição e depois parar a verificação.
5 - se não , adicionar idade a lista.
5 - mostrar lista ordenada

---
## Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,

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

## Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.

No final, mostre os valores pares e ímpares em ordem crescente.

1- Criar uma lista que irá receber 7 números do usuário

2 - A cada volta do for verificar:

    se o número for par, faça:

        inserir na lista em tal posição

    senão, faça

        adicionar na lista

3 - mostrar na tela a lista ordenada em ordem crescente.

 --- 

## Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.


1 - Criar uma lista que vai guardar 3 listas dentro dela e vão ser preenchidas de acordo com os números que o usuário digitar

2 - Entrada do usuário

3 - Fazer um loop de 9 voltas, adicionar os números digitados dentro da primeira sublista.

    - se a primeira sublista atingir 3 números dentro dela, faça:

        adicionar os próximos números dentro da segunda sublista:

    - se a segunda sublista atingir 3 números, faça:

        adicionar os ultimos 3 números na terceira sublista
---

## Exercício Python 089: 
**Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.**

1 -  Preciso de uma lista composta que armazene as seguintes informações para cada aluno:
- Nome
- Nota 1
- Nota 2
2 - criar a entrada do usuário
3 - Criar o cálculo de média
4 - Mostrar como se fosse um boletim no terminal, contendo:
- Nome, nota 1, nota 2, e a média
5 - mostrar cada boletim individualmente - pode ser atráves de um menu de escolha
--- Boletim escolar ---
[1] - Mostrar Boletim de um aluno específico
[2] - Mostrar todas as notas
[3] - Sair 

1 - Ler o nome e duas notas
2 - adicionar o nome e as notas em uma sublista a cada volta do loop, tamanho da sublista = 4 informações no máximo
3 - Fazer o cálculo de média das notas e colocar em sua devida posição em cada sublista(no final)
4 - fazer a validação  de saída
5 -fazer o menu de opções se atrelar com as informações, e mostrar como um boletim mesmo

