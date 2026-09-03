from os import system
system('cls')


def ficha(jogador="", gols = ""):
    
    jogador = input('Nome do jogador: ').strip().capitalize()
    
    if jogador != "":
       jogador = jogador
    else:
       jogador = ""
       
    gols = input('Quantos gols o jogador marcou? ')
    
    if gols != "":
        gols = int(gols)        
    else:
        gols = ""
        
        
    if jogador == "" and gols == "":
        print(f'{'='*13}FICHA DO JOGADOR{'='*13}')
        print('Não há informações sobre esse jogador')
        
    elif jogador == "":
        print(f'{'='*13}FICHA DO JOGADOR{'='*13}')
        print(f'O nome do jogador é: [desconhecido] e ele marcou {gols} gols')     
           
    elif gols == "":
        print(f'{'='*13}FICHA DO JOGADOR{'='*13}')
        print(f'O nome do jogador é: {jogador} e ele marcou [0] gols')
    else:
        print(f'{'='*13}FICHA DO JOGADOR{'='*13}')
        print(f'O nome do jogador é {jogador} e ele marcou {gols} gols')
    
ficha()