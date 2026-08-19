from os import system
system('cls')


#Exercício 027 usando True e break
sum_total = counter = 0
while True:
    number = int(input('Digite um número: '))
    if number == 999:
        break
    counter += 1
    sum_total += number
print(f'Você digitou {counter} números, e a soma entre eles é {sum_total}')
    