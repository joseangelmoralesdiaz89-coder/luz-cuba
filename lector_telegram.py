# SCRIPT PARA TU PC O SERVIDOR
import requests
from telethon import TelegramClient, events

# Reemplaza con tus datos de my.telegram.org
api_id = 'TU_ID'
api_hash = 'TU_HASH'
canal = 'EmpresaElectricaHabana'

client = TelegramClient('luz_cuba', api_id, api_hash)

@client.on(events.NewMessage(chats=canal))
async def handler(event):
    texto = event.raw_text.lower()
    bloques = ["bloque 1", "bloque 2", "bloque 3", "bloque 4"]
    
    for b in bloques:
        if b in texto:
            tema = f"apagones_cuba_{b.replace(' ', '')}"
            # Envío a ntfy.sh
            requests.post(f"https://ntfy.sh/{tema}", 
                          data=event.raw_text.encode('utf-8'),
                          headers={"Title": "Alerta de Corte"})

print("Vigilando Telegram...")
client.start()
client.run_until_disconnected()
