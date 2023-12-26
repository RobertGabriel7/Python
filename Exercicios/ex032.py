import calendar

anoQualquer = int(input('Digite um ano qualquer: '))

# Verificar se o ano é bissexto usando a biblioteca calendar
if calendar.isleap(anoQualquer):
    print("{} é um ano bissexto.".format(anoQualquer))
else:
    print("{} não é um ano bissexto.".format(anoQualquer))
#FEITO GRAÇAS A DEUS