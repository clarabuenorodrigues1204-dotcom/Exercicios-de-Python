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

 Nível 6 — Misturando tudo

## Sistema de notas

Cadastre alunos e suas notas.

Depois mostre:

- [x] Média de cada aluno; 
- Maior média; 
	- fica dentro da lista de alunos aprovados - ordenado - mostrar media na escolha
- Menor média; 
	- menor fica dentro da lista de alunos reprovados - ordenado - mostrar media na escolha
- Alunos aprovados;
- Alunos reprovados.
**Foco:** listas aninhadas, loops e cálculos.

---

## 14. Contagem de caracteres

Receba uma frase e informe:

- Quantidade de caracteres;
- Quantidade de espaços;
- Quantidade de vogais;
- Quantidade de consoantes.

**Foco:** percorrer strings.

1 - Criar entrada do usuário, que vai ser do tipo string
2- Percorrer a frase toda e voltar na tela a quantidade de caracteres ela apresenta   - função len()
3 - Criar contadores para guardar quantos espaços tem na frase, quantas vogais tem na frase e quantas consoantes tem na frase
4 - Mostrar na tela

---


## 15. Palíndromo - (Já tinha feito antes, então vai ser só revisão do código)

Leia uma palavra ou frase e descubra se ela pode ser lida da mesma forma de trás para frente.

**Foco:** strings, índices e listas. 

- **Como a frase é percorrida?**
	-  for i in range(len(junto) - 1, -1 , -1)  - `len()` - 1 retorna a **quantidade de elementos**, e o -1 serve para encontra o **índice do último elemento**. o segundo -1 é o **limite de parada**. O terceiro -1 serve para dizer ao programa "vá diminuindo 1 a cada repetição."
	- inverso += junto[i] - é um acumulador de string, eu não estou somando as letras e sim juntando/concatenando elas em uma coisa só mas mantendo a frase ex: araraarara

- **Como você verificou se era igual ao contrário?**
	- usando um if, se o inverso que é (ex: arara) for igual ao junto (ex: arara) então é um palíndromo, se não, não é um palíndromo
	-
- **Qual método de string você usou?**
		- replace()
		- strip()
		- split()
		- join()
		- lower()
		- len() - pode ser usada em outros locais sem ser string
	
- **Onde entra o `for`?**
	`for`: percorre, um por um, os índices fornecidos pelo `range()` e repete o bloco de código para cada índice.
	
- **Onde entra o `if`?**
	**`if`** → compara a string original (`junto`) com a string invertida (`inverso`) para verificar se são iguais e determinar se a palavra/frase é um palíndromo.
	
- **O que acontece com espaços e letras maiúsculas/minúsculas?**
	os espaços desnecessário são tirados com o .strip() (mas apenas os espaços do início e do final da string) o .lower() transforma a frase em minúsculo, .join() concatena os elementos de uma sequência em uma única string, utilizando a string que chamou o método como separador.

---
# Desafio final — Cadastro completo

Crie um sistema que permita:

- Cadastrar números;
- Impedir números duplicados;
- Remover números;
- Pesquisar um número;
- Mostrar números pares;
- Mostrar números ímpares;
- Mostrar maior e menor;
- Mostrar a lista ordenada;
- Contar quantos números existem;
- Encerrar através de um menu.

### Regra extra

> Não utilize `sort()` nem `sorted()` para fazer a ordenação.

**Foco:** praticamente tudo que foi estudado até aqui.


---
## Exercício Python 091: 
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

1 - Criar um dicionário vazio com o nome (resultado_dados) e adicionar os 4 resultados aleatórios dentro dele
2 - ordenar esse dicionário de alguma forma, opções:
- sorted
- adicionar os resultados dentro de uma lista e depois ordenar
- 3 - adicionando já na ordem correta
3- mostrar no terminal qual foi o jogador que tirou o maior valor no dado

---

## Exercício Python 092: 
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

1- Criar um dicionário vazio
2- Criar entrada do usuário "Nome" , "Ano de nascimento , "Carteira de trabalho"
3- importar a biblioteca que permite obter o ano atual - **datetime** -  calcular a idade e adicionar na chave idade.
4 - Se o CTPS != de 0 faça:
- adicionar duas chaves novas na ficha do usuário que será: "Ano de contratação" e "Salário"
-senão:
- mostrar apenas as informações atuais do usuário
5 - Depois de adicionar a chave idade, devemos fazer o cálculo de quantos anos faltam para o usuário aposentar
6- fazer interface do terminal bonitinha
7- Mostrar informações no terminal
###### Próximos passos

**1 — Criar uma interface para acessar as fichas**

- Mostrar uma lista dos cidadãos cadastrados.
- Permitir escolher qual ficha visualizar.
- Usar o índice da lista para localizar a ficha.

**2 — Melhorar a apresentação da ficha**

- Colocar o nome do cidadão no título.
- Fazer o `for` percorrer as fichas e mostrar cada uma com seu respectivo nome.

Exemplo da ideia:

```
═════════════════════════════════════════════
       FICHA COMPLETA — CLARA BUENO #1
═════════════════════════════════════════════
```

**3 — Salvar os cadastros em JSON**

- Fazer os dados continuarem existindo mesmo depois de fechar o programa.
- Ao iniciar o programa, carregar os cadastros existentes.
- Ao cadastrar uma pessoa, atualizar o arquivo.

**4 — Criar uma barra de pesquisa**  
Permitir pesquisar uma pessoa pelo:

- Nome
- CPF

Aqui você vai começar a trabalhar com algo bem interessante: **percorrer a lista de dicionários e comparar os valores das chaves**.

**5 — Criar validações dos dados**

Por exemplo:

- Não permitir ano de nascimento impossível.
- Não permitir salário negativo.
- CPF com quantidade incorreta de dígitos.
- Não permitir CPF duplicado.
- Não permitir opções diferentes das disponíveis.
- Verificar se o ano de contratação faz sentido em relação ao nascimento.

6- fazer distribuição de funções e começar a tornar esse exercício em um mini programa de cadastro real

---
## Exercício Python 093
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

1- Criar um dicionário vazio com os nome - ficha_jogador = { }
2 - Criar 4 entradas que serão: nome_jogador, quant_partidas, gols_feitos, total_gols.
3 - Quando ele der a quantidade de partidas jogadas, fazer um for repetir a quantidade de partidas que ele registrou, e dentro desse for ele vai pedir o tanto de gols de cada partida.
4 - criar lista que vai armazena o dicionário com as informações do jogador
4- mostrar ficha completa com o total de gols da temporada

---
## Exercício Python 094
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

1 - Criar um dicionário temporário vazio chamado - ficha_tempo = { }
2 - Criar uma lista vazia que vai receber cada dicionário
3 - Se dicionário chegar ao total de 3 informações, adicionar a lista
4 - criar uma variável contadora contar quantas pessoas foram cadastradas
5 - media de idade que vai ser - idades / pelo total de pessoas cadastradas (só vai ser feito depois de saber o total de pessoas)
- Fazer um for k, v in enumerate(lista tal)
- criar uma lista vazia que terá somente as idades
6 - fazer uma lista só para as mulheres
7 - uma lista somente com pessoas que tenha a idade acima da média de idades 

---
## Exercício Python 096
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

1 - Definir uma função que vai se chamar (area) e vai receber como parâmetro:
- b - base
- h - altura
- calculo = b x h
ou:
definir função area sem parâmetro e criar variáveis dentro dela com o nome de b e h e fazer o calculo
2 - fazer a entrada do usuário
3 - chamar a função

---
## Exercício Python 097
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.     

Ex:                                                                                                                                                                        escreva(‘Olá, Mundo!’) Saída:                                                                                                                          ~~~~~~~~~                                                                                                                                         Olá, Mundo!                                                                                                                                          ~~~~~~~~~ 
1 - Definir uma função chamada escreva()
2 - fazer a entrada do usuário ou definir a frase e guarda em uma variável
3 - verificar o tamanho do texto e multiplicar o tamanho pelo '='
4 - mostrar na tela

---
## Exercício Python 098
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:             

a) de 1 até 10, de 1 em 1                                                                                                                      b) de 10 até 0, de 2 em 2                                                                                                                      c) uma contagem personalizada

1 - Criar uma função chamada contador() que terá 3 parâmetros:
- inicio
- meio
- fim
2 - criar um for in range (1,10,1):
- de 1 até 10, pulando de 1 em 1
3 - criar um for in range(10, -1 , -2):
- de 10 até 0, pulando de 2 em 2
4 - criar um for in range(personalizado)
5 - mostrar na tela

---
## Exercício Python 099
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

1 - Criar uma função com o nome "maior()" que terá varios parâmetros dentro dela
2 - já que eu não sei a quantidade de valor, vou usar o empacotador
3 - fazer um comparador e um contador
4 - mostrar na tela

---
## Exercício Python 100
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

1 - criar uma lista vazia chamada número
2 - criar a função sorteia() que terá dentro dela um randint que irá sortear 5 números e depois colocar eles dentro da lista criada
- return numeros
3 - criar a função soma_par() que será responsável por:
	pares = 0
- for valores in numeros:
	- se os valores sorteados  forem %2 == 0, faça:
		somar esses valores e mostrar na tela o resultado
		pares += valores
- return pares
---

## Exercício Python 101
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

1- Criar a função voto() que vai receber como parâmetro o ano de nascimento
2 - importar biblioteca datetime para pegar o ano atual
3 - fazer uma verificação
-
- senão, se a idade >= 65, faça
	- print("voto opcional")

 - se a idade da pessoa for >= 18, faça
	- print("voto obrigatório")

- senão, faça
	- print("voto não obrigatório")

---
## Exercício Python 102
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

1-  Criar uma função chamada fatorial(), que irá receber dois parâmetros - o número que será calculado o fatorial e o outro chamado show
2 - criar a entrada do usuário aonde ele colocará o número para ser fatorado
3- criar a escolha do usuário em relação se vai ou não mostrar o processo de calculo
- se a resposta for [ 1 ] - Mostrar processo de cálculo
- senão, se a resposta for [ 2 ] - Mostrar somente o resultado
4 - Fazer validação referente a número negativo
- se o valor dado pelo usuário for negativo faça:
	- Não existe fatorial de número negativo
- senão, faça:
	- continue
5 - opcional: usar a biblioteca math.factorial()
	- usar o while invés da biblioteca
	- usar o for invés da biblioteca

---
## Exercício Python 103
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

1. OBJETIVO
   O que o programa precisa fazer?
	- O PROGRAMA PRECISA MOSTRAR A FICHA DO JOGADOR, INDEPENDENTE SE ELE FORNECEU O NOME E O NÚMERO DE GOLS

3. ENTRADAS
   Quais informações entram?
	- Nome do jogador e o número de gols marcados

5. REPRESENTAÇÃO
   Como cada informação será representada?
	- jogador - parâmetro 1
	- gols - parâmetro 2
   Qual o tipo?
	- jogador = string
	- gols = int -> vai iniciar como uma string vazia e irá ser convertido em int
   O que representa ausência?
	- jogador = "" -> representa vazio
	- gols = 0

7. CASOS / REGRAS
   Quais situações diferentes podem acontecer?
	- ficha("Pedro" , 4)
	- ficha(" ", 5)
	- ficha("Pedro", [vazio] )
	- ficha(" ", [vazio])

9. PROCESSAMENTO
   O que preciso fazer com os dados?
	-  devo verificar se o usuário forneceu ou não as informações respectivas, fazer verificação para cada caso possível
10. SAÍDA
   O que deve ser produzido?
	- deve ser mostrado o nome do jogador e o número de gols marcado, mas se não houver nome, ou não houver número de gols, fazer uma saída personaliza  
11. CASOS DE TESTE
   Com quais valores vou verificar minha lógica?
	- nome: Pedro
	- gols: 5
	- nome: " "
	- gols 3
	-nome: "Pedro"
	- gols: [vazio]
	- nome: " "
	- gols:[vazio]


