notasDosAlunos =  input('Digite as notas dos alunos separadas por virgula: ').split(',')

notasEmFloat = []
soma = 0

for nota in notasDosAlunos: 
    notasEmFloat.append(float(nota))
    soma += float(nota)

media_final = soma / len(notasEmFloat)

print(f'Media final da turma: {media_final:.2f}')