# androidhelper
Comandos simples relativos ao androidhelper disponível no IDE QPython 3L.

#### Este texto foi retirado e adaptado de < https://gist.github.com/git-jr/80ad698fe55d1ff4be4a6c5a376a32f8 >. O referido autor está disponível em < https://gist.github.com/git-jr >.

#### Para saber mais sobre o androidhelper, vide sua documentação (disponível em < https://kylelk.github.io/html-examples/androidhelper.html > para visualização).

##

```
import time
import androidhelper
droid = androidhelper.Android()

texto = "Texto padrão"
msg = "Alguma mensagem aqui"
tempo = 500
```

* ## Sistema

**Colocar algo no Copiar e Colar**

`droid.setClipboard(texto)`

**Ver o que está no copiar e colar**

`print(droid.getClipboard().result)`

**Vibrar o celular, colocar tempo em millisegundos (1000 = 1s)**
```
droid.vibrate(tempo)

for i in range(5):
    print(i)
    droid.vibrate(tempo)
    time.sleep(1) # Espera um pouco para dar tempo da vibração acabar
```

**Ligar / Desligar Wifi**
```
droid.toggleWifiState(True)

droid.toggleWifiState(False)
```

* ## Interface
```
import sys
import androidhelper
droid = androidhelper.Android()
```

**1 - Mostrar mensagem com Toast**
```
droid.makeToast("Pode ser qualquer texto")
droid.makeToast(texto)
```

**2 - Caixa para entrada de texto**

`droid.dialogGetInput("Titulo", "Mensagem")`

**Mostrar o alerta**

`droid.dialogShow()`

**Pegando o resultado da seleção**
```
escolha = droid.dialogGetResponse().result

droid.makeToast(f"Você digitou: {escolha['value']}")
```

**3 - Criando um a tela de alerta com opções**
```
droid.dialogCreateAlert(
    "Titulo do alerta",
    "A mensagem é, você quer sair?")
```

**Colocando botões**
```
droid.dialogSetPositiveButtonText("Sim")
droid.dialogSetNegativeButtonText("Não")
```

**Mostrar o alerta**

`droid.dialogShow()`
 
**Pegando o resultado da seleção**

`escolha = droid.dialogGetResponse().result`

**Mostrando o resultado**

`print(f"A escolha foi: {escolha['which']}")`

**4 -  Mostar seletor de data**
```
droid.dialogCreateDatePicker()
droid.dialogShow()
```

**5 - Seleção de um valor**

`droid.dialogCreateSeekBar(1, 100, 'Escolha', 'Mensagem')`

**Colocando botões**
```
droid.dialogSetPositiveButtonText("Ok")
droid.dialogSetNegativeButtonText("Cancelar")
droid.dialogShow()

escolha = droid.dialogGetResponse().result
```

**Mostrando o resultado**

`print(f"A escolha foi: {escolha['progress']}")`
