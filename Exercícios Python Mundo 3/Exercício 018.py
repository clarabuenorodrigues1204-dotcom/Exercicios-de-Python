from os import system
system('cls')

ficha = {}
#Adiciona o nome do aluno(a) na chave "nome" e adiciona a média do aluno na chave "media"
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input('Média: '))
print(f'{'='*30}')
#faz a verificação. Se o valor da media for >= 6, ele coloca na chave "status" o valor aprovado, senão, altera a "status" para reprovado
if ficha['media'] >= 7:
    ficha['status'] = 'APROVADO(A)'
    
elif ficha['media'] >= 5 <= 7:
    ficha['status'] = 'RECUPERAÇÃO'
    
else:
    ficha['status'] = 'REPROVADO(A)'
    
print(f'Aluno(a): {ficha["nome"]}\nMédia do aluno(a): {ficha["media"]}\nStatus: {ficha["status"]}')
print(f'{'='*30}')
