from os import system
system('cls')

print('=-' * 30)
print('LISTA DE TIMES DO BRASILEIRÃO')
print('=-' * 30)

print('Lista comprela:')
times_brasileirão = (
    'Flamengo',
    'Palmeiras',
    'Cruzeiro',
    'Mirassol',
    'Bahia',
    'Fluminense',
    'Botafogo',
    'São Paulo',
    'Bragantino',
    'Ceará',
    'Atlético-MG',
    'Internacional',
    'Grêmio',
    'Vasco',
    'Santos',
    'Vitória',
    'Corinthians',
    'Fortaleza',
    'Juventude',
    'Sport'
)

for time in times_brasileirão:
    print(f'- {time}')
print('-' * 30)

print('\nOs 5 primeiros times:')
for time in times_brasileirão[:5]:
    print(f'- {time}')
print('-' * 30)

print('\nOs 4 últimos times:')
for time in times_brasileirão[-4:]:
    print(f'- {time}')
print('-' * 30)   

print('\nOs times em ordem alfabética:')
for time in sorted(times_brasileirão):
    print(f'- {time}')
print('-' * 30)
print(f'\nO São paulo está na posição {times_brasileirão.index("São Paulo")+1}°')
