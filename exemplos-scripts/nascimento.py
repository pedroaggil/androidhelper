# Sistema que formata a data de nascimento de duas formas:

import androidhelper

droid = androidhelper.Android()

dia = input('Em que dia você nasceu? ')
mes = input('Em que mês você nasceu? ')
ano = input('EM que ano você nasceu? ')

mesStr = 0

if mes == 1:
	mesStr = 'janeiro'

elif mes == 2:
	mesStr = 'fevereiro'

elif mes == 3:
	mesStr = 'março'

elif mes == 4:
	mesStr = 'abril'

elif mes == 5:
	mesStr = 'maio'

elif mes == 6:
	mesStr = 'junho'

elif mes == 7:
	mesStr = 'julho'

elif mes == 8:
	mesStr = 'agosto'

elif mes == 9:
	mesStr = 'setembro'

elif mes == 10:
	mesStr = 'outubro'

elif mes == 11:
	mesStr = 'novembro'

elif mes == 12:
	mesStr = 'dezembro'

else:
	mesStr = 'erro'

if mes != 10:
	if mes != 11:
		if mes != 12:
			mes = '0%s' % mes

extenso = 'Você nasceu no dia', dia, 'de', mesStr, 'no ano de', ano
data = dia, '/', mes, '/', ano

droid.ttsSpeak(extenso)
print(data)