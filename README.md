
# Gerador de Mensagens Automáticas WhatsApp

 O código é um exemplo de automação para envio de mensagens usando a biblioteca pywhatkit no Python.

Funcionalidades
O código possui as seguintes funcionalidades:

### Importar bibliotecas necessárias:

```
import pywhatkit
import keyboard
import time
from datetime import datetime
```


### Definir para quais contatos iremos enviar as mensagens:
```
# Números de pessoas usar +55 para código do país, em seguida o DDD da operadora e depois o número da pessoa
lista_envio = ['+551111111111', '+551111111111']
```

### Definir intervalo de envio e enviar as mensagens:

```
while len(lista_envio) >= 1:
    # Enviar mensagens (Espera 1 minuto a partir do momento atual para enviar a mensagem)
    pywhatkit.sendwhatmsg(lista_envio[0], 'Vamos automatizar tudo!', datetime.now().hour, datetime.now().minute + 1)
    del lista_envio[0] # Excluir contato da lista depois da mensagem enviada
    time.sleep(30) # Esperar segundos até o envio da próxima mensagem
    keyboard.press_and_release('ctrl + w') # Fechar a aba do navegador depois do envio da mensagem
```   
### Utilização

Para utilizar o código, siga os passos abaixo:

1. Certifique-se de ter as bibliotecas necessárias instaladas em seu ambiente de desenvolvimento.

2. Atualize a lista lista_envio com os números de telefone dos contatos para os quais deseja enviar as mensagens.

3. Execute o código.
4. Aguarde o envio das mensagens para os contatos especificados.

Lembre-se de respeitar as regras de envio de mensagens automatizadas e a política de privacidade dos destinatários.

### Observações
* Certifique-se de ter uma conexão com a internet para o envio das mensagens.

* O código utiliza o pacote `pywhatkit` para enviar as mensagens pelo WhatsApp. Certifique-se de ter o WhatsApp Web aberto no navegador durante a execução do código.

* O código fecha a aba do navegador após o envio de cada mensagem, utilizando a biblioteca `keyboard`. Certifique-se de que o navegador esteja configurado corretamente para fechar a aba com o atalho Ctrl + W.

**Atenção**: Este código tem como objetivo fornecer um exemplo de automação e não deve ser utilizado para envio de spam ou qualquer atividade ilegal. Utilize-o de forma responsável e respeitando as políticas e regulamentos aplicáveis.
