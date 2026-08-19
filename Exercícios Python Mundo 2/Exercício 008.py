from os import system
system('cls')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
calculo_imc = peso/(altura**2)

if calculo_imc < 18.5:
    print(f'O seu IMC é de: {calculo_imc:.1f} Você está ABAIXO do peso ideal')

elif calculo_imc  < 25:
    print(f'O seu IMC é de: {calculo_imc:.1f} Você está no seu PESO IDEAL')

elif calculo_imc  < 30:
    print(f'O seu IMC é de: {calculo_imc:.1f} Você está com SOBREPESO')    

elif calculo_imc < 40:
    print(f'O seu IMC é de: {calculo_imc:.1f} Você está com OBESIDADE')

else:
    print(f'O seu IMC é de: {calculo_imc:.1f} Você está com OBESIDADE MORBIDA')   