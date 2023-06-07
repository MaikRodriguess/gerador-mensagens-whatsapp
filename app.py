# 1. Importar bibliotecas necessárias
import pywhatkit
import keyboard
import time 
from datetime import datetime
# 2. Definir para quais contatos iremos enviar as msgs 
    # Números de pessoas usar +55 para código do pais, em seguida o DDD da operadora e depois o número da pessoa
lista_envio = ['+5511999394184', '+5569984833424'] 
# Definir intervalo de envio 
while len(lista_envio) >= 1: # Envio a mensagem se tiver pelo menos 1 contato na lista de envio 
    # Enviar mensagens (Espera 1 minuto apartir do momento atual para enviar a mensagem)
    pywhatkit.sendwhatmsg(lista_envio[0], 'Vamos automatizar tudo!', datetime.now().hour, datetime.now().minute + 1 )
    del lista_envio[0] # Exclui contado da lista depois da mensagem enviada
    time.sleep(30) # Espera segs ate envio de proxima mensagem
    keyboard.press_and_release('ctrl + w') # Fecha a aba do navegador depois do envio da mensagem
# 4 Testar! 