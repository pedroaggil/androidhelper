# Sistema que diz em voz alta alguma frase digitada pelo usuário.

import androidhelper

droid = androidhelper.Android()
mensagem = droid.dialogGetInput('Voz!', 'O que você quer que eu diga?').result
droid.ttsSpeak(mensagem)