# Sistema que dá um "bom dia"

import androidhelper

droid = androidhelper.Android()
nome = input('Qual o seu nome, lindeza? ')
msg = 'Que seu dia seja ótimo, %s!' % nome

droid.ttsSpeak(msg)
print(msg)