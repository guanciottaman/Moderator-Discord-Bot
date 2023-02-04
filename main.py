from datetime import time, timedelta, datetime
import discord
from discord import ui
from discord.ext import commands
from discord import app_commands
import asyncio
import pyChatGPT
import aiosqlite
import topgg
#from keep_alive import keep_alive
bot = commands.Bot(command_prefix='!',intents = discord.Intents().all())

session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..bUUxvmgtqRutQyLg.fxZXCleZcve7xMVOaWYj9EchGLWqGp4JTkWyHCgp94-_-VG5i_SuyYp96Ma_Wl15gsize7hp7rV4T5pCcxbsGdrxshTqRff0B8bIVidW6HRhhrcjauf036oojJToUtJXcG_pzXWtAyigL_bqNKVWRaLLc5-9ceR0y5HSpwgUPqYoYfhdhdZgIr3ZPNCa92Lat8DVyh784C1miHmmJoS9YnGTrclGAZ9Tpv7AEvmMTGxt1VWPmpFJPXiSxxnantCkvQMGIcNJ9EvgJPWynQpriI5wNB7oBGTD43l-jHj69uIHkT6Gl1chn5-YwU4e5pyPYSMR4w80ychIaTvnHoNOqqMddmjinJZq60qrHoFJ_lZqQLOfy84b07xiT2QiEDbdy9ebqzC3vIGN61rJtovHBzTOrb26rghobC9Ae3DQTkEnYA6aZG4ZR0KPzCAHYFCJo0chElJp5NntUMOf_s1UCRrBuubjawbVz7LbCTYbPkxl2bDymRYfhxh1M1I-8qNwjCOrCL8b_X6fTVeb1VU_USPnNHitO_JMeJ2YZfJjXuGMDnJhJiR_DYYqS7p6BpIjOMJ7HBhS8wRwIlsvwjAvu3EbD7TxbJtEufJKk1yM4faBwyN7ZyN6UfpA1Kc195FahpTcZmaHgNWAnLCCvm9EEmPltB73Cb4QQsKXUSOMt_xV0nJxgbmNZAbYpV5ma7_1N1h8svbqYJ1Pyxe1Hi8NyTGie8ykMjbDaYaAAUtRbQ318uJ7dVHzk7Fz45dSXH9Sjtsy6rUE86KzwIvqJIdQl8j7Epu6X34v9ExItF0q8IwNxOibKFpLkXXux5Zkdw77007h5VNljHi_MgiMP49nB9KpbWfEahiCi50phB_9Vi6HNuKydAFiYaRDQsL_ymjkvnRLlNU0WGz40IjBdhRMKEikru1tTdr0XRK2mi8uwqbQa3bPcpc5-VvEE6_GAbzLPgDXdOa6qS1y0zRBIbf0QCG5etLkCpjos66g6CJ2h7nhwkyJN_j2oIjhOVf3xBEKaIGf4mrVYK8J4uwW7ek1z-jBupX9BgKJ2Ea1SKp-G6tAT-tuZrq5HhyIrIKBXPLQz-3xxHarMQ7pUvxIhNh7ueE_vZXqtBBV_eQIBV3FyAHZNSqVhOIdg9wOWORcjg_8hPLZv-V9JMe9J1JUS6SQPeSDInABl_G40todP3jCtOleBF-BtAWycEFiGZCMhxRhDuOND33-LVChXZLdFheeIYrJvwBdW-VPpni3MfUNWjFjMoXcRsUrH0SdpqATwFk-dHRAs4XKXn-5u7corEzSeqHDCEuYyjnmF9HNjCqhEXHqwcuA8nrvKHzD9ViEfq6C8-j5PcAWU1ozk8USoTJNes6zWNUlEND3nMEUDj_2TVzEysxm7oKCb9e1ak13loyGqwQl-A3-Qffu6mwWQMxBCBxfkvs6u2QOUwV0ee1aqrvtEKIvVeUgaHPXtbE2gzFCw_argMsnozrSNQUWKb-wMY4qpZ71WCI8uG84qaAAD3FBZOwEcEaXI45bL80621DgIowDkEFn1OrjnplEg87U37haApZA-2q2UZEIqHYxZIpsXigprhWPPVn1rIadb0xlhbwirgFAu1-ctlLiQfo18wPy1ISyALhsaBXGxgI8ky-6rjAxLxFAJgQmLrgnUb8oDH1MM7hW0Ec-eeR_M8JZUvXS9tX5-_jsn5VJCkm9-rC_Q-nEwOMHWyy_qk8wjSFy0yU91IBtl1ILs0JOdpBGQwRMIib3D-LrtWFiBTfXMTxGCOoxtWzueqoPr5yk1wsK9637jykhQ6MkuY_JIkiI6umSI0wZTWexxn4ftggU4OvQqCTQTenaKhF3h-6M-W1fjKYHlKetJ9jEPAi8-in_3UJajg8EFUE3iaJjHW0iiKV90-6jbcYaEMSJL1Phceorv7uhtq4Wb9yKa8QlZNsvFlIpaLSrze_YhsQJyyrqa0KaIUkU-48qtuAK_vg57nLYAeib7Uehkpew9uSv4mFsN8UgwckO-MxdLBv7LcpNzcbypzuUcHCx7ERa-XVbfPg4ElN8Ttu1qkgCjIWPBEOQ-AUV7-yrk_BYtaaZjQmSwAJdzRX9QtQ2I-m4OUgDubkxryrkJlxQomaYTNe1kMhv-1noD-F9RQDvfCsyf4EiZ6P1lY52HpJDS9QdBVVLe6XFV78rnCCNomL_86bVeUWIwJlB5A4tctkuR6CZHUoZsPQMUVu7vxo2g6u29ZI7kRTG4KNBLm1YICUrk9Hhjjzo0z8wbn1wuuW1jiCVZCfO8TpIF6KLU3pJzLvMNoIEEwxeCFMUe2ujF34wQCpzKWHSBaXVlB9idWHneN49mZ2SxqzXOBaPZCHcCkeMBrm6eTuLLCShgSaORzvpuf7ZwWuy1mJSwH1v8eiq7fsVRLBXeIt1mwGRsWo5gJaAo5yBVsS1d-liEGzdxmXuKGyD6S11q5JVaArYS9W9XuiTfoT56oB4OwFKqkm5-V3n-iBBD5spBtElwDZxpu0SCoB2Llgn8ltnAAg9wHf1h1fzTWU56CUhV3oF_2k4gJopmXHUolvvX3SBAeJcq7YpOmC6xq8W7kGSDDNhiWiIhxSSfZE._tgAo63ZXk_whn5kx6UMVw'

session_api = pyChatGPT.ChatGPT(session_token=session_token)

token = 'MTAwNzU2OTQxMDc0NTE3MjAxOQ.GWRHBH.bfjmYTDIo5loWrkNXkGtXFxxMhR0IjD4dePRps'

dbl_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEwMDc1Njk0MTA3NDUxNzIwMTkiLCJib3QiOnRydWUsImlhdCI6MTY3NTU0MDk5MX0.69k1q7D2BSlUuUiHR_wxnWI8xZBllho-5dVgALInBX4"  # set this to your bot's Top.gg token
bot.topggpy = topgg.DBLClient(bot, dbl_token, autopost=True, post_shard_count=True)




class BandoMod(ui.Modal, title='Bando staff'):
    nome = ui.TextInput(label='Nome', placeholder='Inserisci il tuo nome', style=discord.TextStyle.short, max_length=30)
    eta = ui.TextInput(label='Età', placeholder='Inserisci la tua età', style=discord.TextStyle.short, max_length=6)
    ruolo = ui.TextInput(label='Per quale ruolo ti candidi?', placeholder='(Grafico, Developer, Moderatore...)', style=discord.TextStyle.short, max_length=20)
    motivo = ui.TextInput(label='Perchè vuoi candidarti da noi?', placeholder='Voglio candidarmi perchè ...', style=discord.TextStyle.long, max_length=250)
    async def on_submit(self, interaction:discord.Interaction):
        emb = discord.Embed(title='Bando Mod', description=f'**{self.nome.label}**\n {self.nome}\n\n **{self.eta.label}**\n {self.eta}\n\n **{self.ruolo.label}** \n {self.ruolo} \n\n**{self.motivo.label}**\n {self.motivo}', color=discord.Color.from_rgb(255, 0, 0))
        emb.set_author(name = interaction.user, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=emb)

class Client(commands.Bot):
    def __init__(self):
        intents = discord.Intents().all()
        super().__init__(command_prefix=commands.when_mentioned_or('!'), intents=intents)
        self.antispam = commands.CooldownMapping.from_cooldown(10, 20, commands.BucketType.member)
        self.too_many_violations = commands.CooldownMapping.from_cooldown(3, 60, commands.BucketType.member)
        ####self.countfile = open('counting.txt','a+')
        ###self.countfile.seek(0)
        ##self.lines = self.countfile.readlines()
        #self.last_number = int(self.lines[-1]) if self.lines else 0
        
    @bot.event
    async def on_ready(self):
        print('Il bot è online')
        try:
            synced = await bot.tree.sync()
            print(f'Comandi sincronizzati: {len(synced)}')      
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=' i bimbi brutti'))
            
        except Exception as e:
            print(e)

    @bot.event
    async def on_autopost_success():
        channel = bot.get_channel(1017762538659778581)
        await channel.send(f"Posted server count ({bot.topggpy.guild_count}), shard count ({bot.shard_count})")

    @bot.event
    async def on_message(self, message):
        if type(message.channel) is not discord.TextChannel or message.author.bot: return
        bucket = self.antispam.get_bucket(message)
        retry_after = bucket.update_rate_limit()
        if retry_after:
            await message.delete()
            await message.channel.send(f'{message.author.name}, non spammare!', delete_after=5)
            violations = self.too_many_violations.get_bucket(message)
            check = violations.update_rate_limit()
            if check:
                await message.author.timeout(timedelta(minutes=1), reason='Spam')
                try: await message.author.send(f'{message.author.name}, sei stato mutato in {message.guild.name}')
                except: pass

        async def setup_hook(self) -> None:
            self.add_view(view())
            self.add_view(view2())
            self.add_view(ticket())


bot = Client()
bot.remove_command('help')

async def connect(loop):
        async with aiosqlite.connect('warns.sql', loop=loop) as conn:
            async with conn.cursor() as cursor:
                await cursor.execute('CREATE TABLE IF NOT EXISTS warns(user INTEGER, reason TEXT, time INTEGER, guild INTEGER)')
                await conn.commit()

class view(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label='Invia', style = discord.ButtonStyle.green, custom_id='1')
    async def callback(self, interaction:discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_modal(BandoMod())


class view2(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label='Ottieni', style = discord.ButtonStyle.blurple, custom_id='2')
    async def callback(self, interaction:discord.Interaction, Button: discord.ui.Button):
        guild = interaction.guild
        ruolo = discord.utils.get(guild.roles, id=1041322926462476349)
        if ruolo not in interaction.user.roles:
            await interaction.user.add_roles(ruolo)           
        else:
            await interaction.user.remove_roles(ruolo)
        await interaction.response.send_message('Hai ricevuto/rimosso il ruolo', ephemeral=True)

class ticket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 120, commands.BucketType.member)
    @discord.ui.button(label='Ticket', style = discord.ButtonStyle.blurple, custom_id='3')
    async def callback(self, interaction:discord.Interaction, Button: discord.ui.Button):
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(f'Non puoi usare questo botton per altri {round(retry, 1)}', ephemeral=True)
        guild = bot.get_guild(1043217543604748290)
        ticketrole = discord.utils.get(guild.roles, id=1059551782721818795)
        modrole = discord.utils.get(guild.roles, id=1046907122627133521)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ticketrole: discord.PermissionOverwrite(read_messages=True),
            modrole: discord.PermissionOverwrite(read_messages=True)
        }
        with open('tickets.txt', 'r+') as f:
            line_count = 0
            f.write('ticket\n')
            for line in f:
                line_count += 1
        channel = await interaction.guild.create_text_channel(name=f'{interaction.user.name} ({line_count})', overwrites=overwrites)
        await interaction.user.add_roles(ticketrole)
        controller = ui.View()
        btnclose = ui.Button(label='Chiudi Ticket', style=discord.ButtonStyle.danger, custom_id='6')
        async def callback(interaction:discord.Interaction):
            await channel.delete()
        btnclose.callback = callback
        controller.add_item(btnclose)
        await channel.send(f'Il ticket {channel.name} è stato creato', view=controller)
        await interaction.response.send_message(f'Il canale {interaction.user.name} è stato creato', ephemeral=True)

class helpview(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label='➡️', style=discord.ButtonStyle.blurple, custom_id='8')
    async def callback(interaction: discord.Interaction, Button:discord.ui.Button):
        emb2 = discord.Embed(title='Help - Page 2',description='\n**Banna(context_menu):** Banna un membro\n\n **Espelli(context_menu):** Espelle un membro\n\n **Informazioni(context_menu):** Informazioni sul membro\n\n **Avatar(context_menu):** Ottieni l\'avatar del membro.\n\n')
        await interaction.response.edit_message(embed=emb2)

    @discord.ui.button(label='⬅️', style=discord.ButtonStyle.blurple, custom_id='9')
    async def callback(interaction: discord.Interaction, Button:discord.ui.Button):
        emb = discord.Embed(title='Help',description='\n**/say:** Fai dire qualcosa al bot.\n\n **/avatar {member}:** Ottieni l\'avatar del membro.\n\n **/ban {member}:** Banna un membro.\n\n **/kick {member}:** Espelle un membro.\n\n **/clear {amount}:** Pulisce la chat.\n\n',color=discord.Color.from_rgb(0, 0, 255))
        await interaction.response.edit_message(embed=emb)

@bot.tree.context_menu(name='Informazioni')
async def identità(interaction:discord.Interaction, member:discord.Member):
    try:
        emb = discord.Embed(title=f'{member.name}', description=f'Ecco alcune informazioni su {member.mention}.', color=discord.Color.from_rgb(0, 0, 255))
        emb.add_field(name='Id', value=member.id, inline=False)
        emb.add_field(name='Su discord da:', value=member.created_at.strftime("Il %d %h %Y alle %H:%M:%S"), inline=False)
        emb.add_field(name='Ruoli', value=', '.join([role.name for role in member.roles]), inline=False)
        emb.add_field(name='Badge', value=', '.join([badge.name for badge in member.public_flags.all()]), inline=False)
        emb.add_field(name='Stato', value=member.activity, inline=False)
        emb.set_thumbnail(url=member.avatar.url)
        btn = ui.Button(label='Download avatar', style=discord.ButtonStyle.url, url=member.avatar.url)
        downloadview = ui.View()
        downloadview.add_item(btn)
        await interaction.response.send_message(embed=emb, view=downloadview)
    except:
        await interaction.response.send_message('Non puoi usarlo sul bot', ephemeral=True)

@bot.tree.command(name='autorole', description='Manda l\'autorole')
async def autorole(interaction:discord.Interaction):
    emb = discord.Embed(title='Ruolo FiveM', description='Clicca il bottone qui sotto per ricevere il ruolo ed accedere alla categoria di FiveM')
    await interaction.response.send_message(embed=emb, view=view2())

@bot.tree.command(name='tickettake', description='Manda il ticket')
async def tickettake(interaction:discord.Interaction):
    emb = discord.Embed(title='Ticket', description='Hai bisogno di assistenza?\n Clicca il bottone qui sotto per creare un ticket', color=discord.Color.from_rgb(0, 0, 255))
    await interaction.response.send_message(embed=emb, view=ticket())

@bot.tree.command(name='bandomod', description='Manda il bando per mod')
async def bandomod(interaction:discord.Interaction):
    emb = discord.Embed(title='Bando Mod', description='Clicca il bottone qui sotto per inviare il tuo bando')
    await interaction.response.send_message(embed=emb, view=view())

@bot.tree.command(name='kick', description='Espelli un membro')
@app_commands.describe(member='Membro da espellere')
async def kick(interaction:discord.Interaction, member:discord.Member):
    emb = discord.Embed(title='Membro espulso', description=f'{member.name} è stato espulso', color=discord.Color.from_rgb(255, 0, 0))
    await interaction.response.send_message(embed=emb)
    await member.kick()

@bot.tree.context_menu(name='Espelli')
async def kick(interaction:discord.Interaction, member:discord.Member):
    emb = discord.Embed(title='Membro espulso', description=f'{member.name} è stato espulso', color=discord.Color.from_rgb(255, 0, 0))
    await interaction.response.send_message(embed=emb)
    await member.kick()

@bot.tree.command(name='ban', description='Banna un utente')
@app_commands.describe(member = 'Membro da bannare', reason = 'Motivo')
async def ban(interaction:discord.Interaction, member:discord.Member, reason:str):
    await member.ban()
    emb = discord.Embed(title = f'{member.name} è stato bannato', description = f'{member.mention} è stato bannato', color=discord.Color.from_rgb(255, 0, 0))
    emb.add_field(name='Motivo:', value=f'{reason}')
    await interaction.response.send_message(embed=emb)

@bot.tree.context_menu(name='Banna')
async def ban(interaction:discord.Interaction, member:discord.Member):
    emb = discord.Embed(title = f'{member.name} è stato bannato', description = f'{member.mention} è stato bannato', color=discord.Color.from_rgb(255, 0, 0))
    await interaction.response.send_message(embed=emb)
    await member.ban()

@bot.tree.command(name='warn', description='Warna un utente')
@app_commands.describe(member = 'Membro da warnare', reason= 'Motivo del warn')
async def warn(interaction:discord.Interaction, member:discord.Member, reason:str='Nessun motivo previsto'):
    """
    guild = bot.get_guild(1043217543604748290)
    warn1 = discord.utils.get(guild.roles, id=1058848864725115020)
    warn2 = discord.utils.get(guild.roles, id=1058848860002324563)
    warn3 = discord.utils.get(guild.roles, id=1058848978604671056)
    if warn1 not in member.roles and warn2 not in member.roles and warn3 not in member.roles:
        await member.add_roles(warn1)
    if warn1 in member.roles:
        await member.remove_roles(warn1)
        emb2 = discord.Embed(title='Warn', description=f'{member.mention} è stato warnato da {interaction.user} per {reason}. Ha 2 warn', color=discord.Color.from_rgb(255, 0, 0))
        await member.add_roles(warn2)
        await interaction.response.send_message(embed=emb2)
    if warn2 in member.roles:
        await member.remove_roles(warn2)
        emb3 = discord.Embed(title='Warn', description=f'{member.mention} è stato warnato da {interaction.user} per {reason}. Ha 3 warn', color=discord.Color.from_rgb(255, 0, 0))
        await member.add_roles(warn3)
        await interaction.response.send_message(embed=emb3)
    if warn3 in member.roles:
        embed = discord.Embed(title = f'{member.name} è stato bannato', description = f'{member.mention} è stato bannato', color=discord.Color.from_rgb(255, 0, 0))
        await interaction.response.send_message(embed=embed)
        await member.ban()
    else:
        emb4 = discord.Embed(title='Warn', description=f'L 'utente è stato già bannato o non è stato trovato', color=discord.Color.from_rgb(255, 0, 0))
        await interaction.response.send_message(embed=emb4)
        """
    await addwarn(interaction, member, reason)
    emb = discord.Embed(title='Warn', description=f'{member.mention} è stato warnato da {interaction.user} per {reason}.', color=discord.Color.from_rgb(255, 0, 0))
    await interaction.response.send_message(embed=emb)

async def addwarn(interaction:discord.Interaction, member:str, reason:str):
    async with aiosqlite.connect('warns.sql', loop=loop) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("INSERT INTO warns (user, reason, time, guild) VALUES (?, ?, ?, ?)", (member.id, reason, int(datetime.now().timestamp()), interaction.guild.id))
            await conn.commit()

@bot.tree.command(name='unwarn', description='Rimuove un warn a un membro')
@app_commands.describe(member='Il membro da unwarnare')
async def unwarn(interaction:discord.Interaction, member:discord.Member):
    """
    guild = bot.get_guild(1043217543604748290)
    warn1 = discord.utils.get(guild.roles, id=1058848864725115020)
    warn2 = discord.utils.get(guild.roles, id=1058848860002324563)
    warn3 = discord.utils.get(guild.roles, id=1058848978604671056)
    if warn1 not in member.roles and warn2 not in member.roles and warn3 not in member.roles:

    if warn1 in member.roles:
        await member.remove_roles(warn1)
        emb2 = discord.Embed(title='Unwarn', description=f'{member.mention} è stato unwarnato da {interaction.user}. Ora non ha warn', color=discord.Color.from_rgb(0, 128, 0))
        await interaction.response.send_message(embed=emb2)
    if warn2 in member.roles:
        await member.remove_roles(warn2)
        await member.add_roles(warn1)
        emb3 = discord.Embed(title='Unwarn', description=f'{member.mention} è stato warnato da {interaction.user}. Ha 1 warn', color=discord.Color.from_rgb(0, 128, 0))
        await interaction.response.send_message(embed=emb3)
    if warn3 in member.roles:
        await member.remove_roles(warn3)
        await member.add_roles(warn2)
        embed = discord.Embed(title = 'Unwarn', description = f'{member.mention} è stato warnato da {interaction.user}. Ha 2 warn', color=discord.Color.from_rgb(0, 128, 0))
        await interaction.response.send_message(embed=embed)
    else:
        emb4 = discord.Embed(title='Unwarn', description=f'L 'utente è stato già bannato o non è stato trovato', color=discord.Color.from_rgb(0, 128, 0))
        await interaction.response.send_message(embed=emb4)
        """
    async with aiosqlite.connect('warns.sql', loop=loop) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute('SELECT reason FROM warns WHERE user = ? AND guild = ?', (member.id, interaction.guild.id))
            data = await cursor.fetchone()
            if data:
                await cursor.execute('DELETE FROM warns WHERE user = ? AND guild = ?', (member.id, interaction.guild.id))
                emb = discord.Embed(title='Unwarn', description=f'Tolto un warn a {member.mention}', color=discord.Color.from_rgb(0, 128, 0))
                await interaction.response.send_message(embed=emb)
            else:
                emb = discord.Embed(title='Unwarn', description=f'{member.mention} non ha warn', color=discord.Color.from_rgb(0, 128, 0))
                await interaction.response.send_message(embed=emb)
        await conn.commit()

@bot.tree.command(name='warnings', description='Mostra i warn di un membro')
@app_commands.describe(member='Il membro da mostrare')
async def warnings(interaction:discord.Interaction, member:discord.Member):
    async with aiosqlite.connect('warns.sql', loop=loop) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute('SELECT reason, time FROM warns WHERE user = ? AND guild = ?', (member.id, interaction.guild.id))
            data = await cursor.fetchone()
            if data:
                emb = discord.Embed(title = f'Warns di {member.name}')
                warnnum = 0
                for table in data:
                    warnnum += 1
                    emb.add_field(name=f'Warning {warnnum}', value=f'Motivo: {table[0]}\n Data: <t{datetime.fromtimestamp(int(table[1]))}:F')
                await interaction.response.send_message(embed=emb)
            else:
                emb = discord.Embed(title='Unwarn', description=f'{member.mention} non ha warn', color=discord.Color.from_rgb(0, 128, 0))
                await interaction.response.send_message(embed=emb)

@bot.tree.command(name='say', description='Fai dire qualcosa al bot')
@app_commands.describe(messaggio = 'Fai scrivere qualcosa al bot')
async def say(interaction:discord.Interaction, messaggio: str):
    await interaction.response.send_message(messaggio)

@bot.tree.command(name='avatar', description='Manda l\'avatar di un membro')
@app_commands.describe(member = 'Membro da taggare con il suo embed')
async def avatar(interaction:discord.Interaction, member: discord.Member):
    Embed = discord.Embed(title=member.mention, color=discord.Color.from_rgb(0, 0, 255))
    Embed.set_image(url='{}'.format(member.avatar.url))
    btn = ui.Button(label = 'Download avatar', style = discord.ButtonStyle.url, url = member.avatar.url)
    view=ui.View()
    view.add_item(btn)
    await interaction.response.send_message(embed = Embed, view=view)

@bot.tree.command(name='clear', description='Pulisce la chat')
@app_commands.describe(amount='Numero di messaggi da eliminare')
async def clear(interaction:discord.Interaction, amount:int=None):
    await interaction.response.defer()
    if amount == None:
        await interaction.response.send_message(f'Sono stati cancellati {amount} messaggi', ephemeral=True)
        await interaction.channel.purge(limit=1000000)
    else:
        try:
            int(amount)
        except:
            await interaction.response.send_message('Per favore inserisci un numero valido(max 1000000).', ephemeral=True)
        else:
            await interaction.channel.purge(limit=amount)
            await asyncio.sleep(1)
            await interaction.response.send_message(f'Sono stati cancellati {amount} messaggi', ephemeral=True)

@bot.tree.command(name='askai', description='Chiedi qualcosa a ChatGPT')
@app_commands.describe(prompt='Messaggio da mandare')
async def askai(interaction:discord.Interaction, prompt:str):
    await interaction.response.defer()
    #await interaction.response.send_message('Si sta generando una risposta...', delete_after=10)
    response = session_api.send_message(prompt)
    # formatting the response
    response = "".join(response.get("message"))
    # printing the formatted response
    await asyncio.sleep(1)
    emb = discord.Embed(title='ChatGPT', description=f'**Hai chiesto:**\n {prompt}\n\n **Risposta:**\n {response}\n', color=discord.Color.from_rgb(0,0,255))
    await interaction.followup.send(embed=emb)

@bot.tree.command(name='help', description='Aiuto')
async def help(interaction:discord.Interaction):
    emb = discord.Embed(title='Help', description='\n**/say:** Fai dire qualcosa al bot.\n\n **/avatar {member}:** Ottieni l\'avatar del membro.\n\n **/ban {member}:** Banna un membro.\n\n **/kick {member}:** Espelle un membro.\n\n **/clear {amount}:** Pulisce la chat.\n\n', color = discord.Color.from_rgb(0,0,255))
    await interaction.response.send_message(embed=emb, view=helpview())

#keep_alive()
loop = asyncio.get_event_loop()
loop.run_until_complete(connect(loop))
bot.run(token)
