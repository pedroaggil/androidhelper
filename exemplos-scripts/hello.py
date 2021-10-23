# Sistema que diz um "olá" de diferentes formas

import androidhelper

droid = androidhelper.Android()
nome = droid.dialogGetInput('Olá!', 'Diga o seu nome:')
msg = 'Olá, %s!' % nome.result
droid.ttsSpeak(msg) # Fala a mensagem
print(msg) # Escreve a mensagem
droid.makeToast(msg) # Alerta, confirmação rápida