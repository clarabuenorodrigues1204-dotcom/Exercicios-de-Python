from os import system
system('cls')

#Conversor de medidas
metros = float(input('Digite um número em metros: '))
km = metros / 1000
hm = metros / 100
dc = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print(f'O valor de metros em KM é: {km}, o valor de metros em HM é: {hm} , o valor de M em DC é: {dc}\n O valor de DM em metros é: {dm} valor de metros em CM é: {cm} , e o valor de metros em MM é: {mm}')

#SEGUNDA MANEIRA
#metros = float(input('Digite um valor em metros:'))
#print = (f'O valor de metros em centímetro é: {metros * 100} , é o valor de metros em milímetros é: {metros * 1000})

numero = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print(f'{numero} x 1 = {numero * 1}')
print(f'{numero} x 2 = {numero * 2}')
print(f'{numero} x 3 = {numero * 3}')
print(f'{numero} x 4 = {numero * 4}')
print(f'{numero} x 5 = {numero * 5}')
print(f'{numero} x 6 = {numero * 6}')
print(f'{numero} x 7 = {numero * 7}')
print(f'{numero} x 8 = {numero * 8}')
print(f'{numero} x 9 = {numero * 9}')
print(f'{numero} x 10 = {numero * 10}')
print('-' * 12)