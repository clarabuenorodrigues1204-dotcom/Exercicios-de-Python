from os import system
system('cls')


num = int(input('Quantos termos você gostaria de mostrar? ')) #Num vai receber um número inteiro que foi dado pelo usuário
num0 = 0 #essa variável vai iniciar em 0, pois é o primeiro termo da sequência
num1 = 1 #essa váriavel vai iniciar em 1, pois é o segundo termo da sequência
contador = 0 #inicia em 0, pois ele quem contará quantas repetições o while já fez.

print('0' , end=' → ')

while num != contador: #Enquanto a quantidade de termos desejada pelo usuário (num) for diferente da quantidade de repetições realizadas (contador), o while continua executando.
    soma = num0 + num1      #Criei variável "SOMA" para somar as duas variáveis que foram inicializadas fora do while
    num0 = num1         #Aqui a varíavel "num0" é atualizada com o valor que está na váriavel "num1", assim guardando o número que estava dentro de num1 e descartando o                    numero anterior.
    num1 = soma         #A varíavel "num1" é atualizada com o valor da soma entre "num0" e "num1" , assim descantando o valor anterior
    contador +=1        #Contador é sempre atualizado com +1 até chegar no total de repetições do while

    print(f'{num0}', end= ' → '  )
print('FIM!')