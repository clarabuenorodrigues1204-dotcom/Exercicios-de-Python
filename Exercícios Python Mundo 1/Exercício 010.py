from os import system
system('cls')

#Media de notas
notas = []
soma = 0
for i in range(5):
    notas.append(int(input('Digite uma nota: ')))   
    
for i in notas:
    soma += int(i) 
media = soma/(len(notas)) 
print(media)


#aluno = float(input('Digite uma nota: '))
#aluno2 = float(input('Digite outra nota: '))
#print(f'A sua média de notas é {(aluno + aluno2) / 2}')