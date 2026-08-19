from os import system
system('cls')

largura = float(input('Largura da parede: '))
altura = float(input('altura da parede: '))
area = largura * altura
print(f'A dimensão dessa parede é {largura} x {altura} e a sua área é de {area} m² \n Para pintar essa parede, você precisará de {area / 2}L de tinta')
