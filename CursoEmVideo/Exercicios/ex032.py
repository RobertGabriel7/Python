import calendar
from datetime import date
anoQualquer = int(input('Digite um ano qualquer (0 para o ano atual): '))

if anoQualquer ==0:

    anoQualquer = date.today().year

# Verificar se o ano é bissexto usando a biblioteca calendar
if calendar.isleap(anoQualquer):
    print("{} é um ano bissexto.".format(anoQualquer))
else:
    print("{} não é um ano bissexto.".format(anoQualquer))
#FEITO GRAÇAS A DEUS