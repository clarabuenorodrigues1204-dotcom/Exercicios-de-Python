from os import system
system('cls')
#Função criada para analisar varias notas
def notas(*num, situacao = False):
    """
    -> Função para analisar notas e situações de vários alunos
    param num: uma ou mais notas dos alunos(aceita várias)
    param situacao: valor opcional indicando se deve ou não adicionar a situação acadêmica do aluno
    return: dicionário com várias informações sobre a situação da turma
    """
    
    #Esse bloco é responsável por: quantidade de notas cadastradas, por pegar o maior e o menor valor, e por fazer a média das notas
    nota = {}
    nota['total'] = len(num)
    nota['maior'] = max(num)
    nota['menor'] = min(num)
    media = sum(num) / len(num)
    nota['media'] = media
    #Esse bloco é responsável pela situação da turma, que pode estar entre 3 tipos: Acima da média, Na media, Abaixo da média
    if situacao:  
        if nota['media'] >= 7:
            nota['Situação'] = 'Acima da média'
        elif nota['media'] >= 5 and nota['media'] < 7:
            nota['Situação'] = 'Na média'
        elif nota['media'] < 5:
            nota['Situação'] = 'Abaixo da média'
        
    return nota

print(notas(10,3.5,6,9,5,situacao=True))


    
    