from os import system
system('cls')


def comando(comandos):
    help(comandos)

def titulo(msg, cor = 0):
    tam = len(msg)
    
    print('='*tam)
    print(f'    {msg.center(tam)}')
    print('='*tam)
    
comandos = ''
while True:
    titulo('\033[32mSISTEMA DE AJUDA PYHELP!\033[m')
    comandos = input('Digite uma função ou uma biblioteca >> ')
    
    if comandos.upper() == 'FIM':
        titulo('FIM DO PROGRAMA')
        break
    else:
        titulo(f'\033[32mSISTEMA DE AJUDA PYHELP - {comandos}!\033[m')
        comando(comandos)

            
        
          
