nomeCompleto = str(input('Digite o seu nome completo: '))

indiceDeNome = nomeCompleto.split()
indiceDeNome1 = nomeCompleto.rsplit()


print('O seu nome completo é "{}"'.format(nomeCompleto))

print('O seu primeiro nome "{}"'.format(indiceDeNome[0]))
print('O seu ultimo nome "{}"'.format(indiceDeNome1[-1]))

#FEITO GRAÇAS A DEUS!