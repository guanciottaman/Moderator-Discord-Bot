from pypresence import Presence
import time

app_id = 1076477726443184210

RPC = Presence(app_id)
RPC.connect()
RPC.update(
    state='Compra i nostri prodotti su FMSHOP!',
    small_image='icon',
    small_text='FM SHOP',
    buttons=[{'label': 'Vai ad acquistarli!', 'url': 'https://fmshop-webshop.tebex.io/'}, {'label': 'Discord', 'url': 'https://discord.gg/VBsqxhFE'}]
    )

while True:
    time.sleep(120)