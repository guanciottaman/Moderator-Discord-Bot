from datetime import timedelta, datetime
from dis import disco
from msilib.schema import Icon
import discord
from discord import ui
from discord.ext import commands
from discord import app_commands
import asyncio
#import pyChatGPT
import matplotlib
import sqlite3
import random
import schedule

# from keep_alive import keep_alive
bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

#session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..H9isWHjQKV6H2erJ.QV7D7-jifV41pVGAi1OpBdp1x-7GyVMzhhIVzP8WQQIo5AjRWIYyYqJQ-ndKk-EF8ftFypXNq7l7N2GW0dyVXO0SrdyqXViPdRFsKIfMIQ0iww93kSsTEDc5R0JS78yhzgCk4RjbnBTtKh2oJMeZxswAmd58B_hJlU0kSuV5PaEryIELHgV8zRfSlnzrCizZf2EX9Wi8kvcr1ZQqrZEuy35X0_yF74EFE554mdj9P-sFY415wLCkEWw1XGg2kDUD-xeL9RF_l2fjuabYL6WdXwAVYb2NKXqc_HbDX-KF-_EUZOy8lbIxaJjuFjZWbnqrCYYbakXGBIc-6sg64xbtLulJ92gLW49ZCQK3_lBL9vk1vn-Z7JAmB_3_ZtpnVuhKREI_ZjemwDvx4J84qH6CsCWQFMYVLgdu7fPybgqgGRzz9dNl7XBg4DgJaNjMn8zFIx-krHft_6rwmF9EQrFIgeyYrExMCkUlE3puhtbylk-dK-ZcQvxslUWL6mxSrvbZAwIhk-gKJbglKl6yobFE474F5ZvMiScdfh_caaZ0nDF0UhOkcffN0Zu7lNg-ZC90O_nmOGyOFen5vh9F73M3FYzvRq2hfwHzV-pp7GoXnpME9mc6OjEGvj167C8LQY540TWlVXaPGzwx9uL7bbvLGqDBhwYFiD_hWr54bttZeiS3inGDeEw6fa4lShcpyFfo9r7TwfdVDj0dm5Aatb5KQsS8YsqubOcPdNMPJbYLhIrS9KxcHbd-vUipVOC2OtDPhrRpOPU_-cYaflECebPV9mZoBaA5LqEFy1SRhaqN5jiazXSI6KENZHfoRyFnyLPoqhW9v5iua4ys0y9jfq6Zb2e12NtrTnJAEvjC8aMwJiQvEOlKcgJFP3fesUZqX0zTgT6Eg4A4wqmO9P3VCBo5uFIudHQOZ92T7pRiYuouHB9NDoV77h9HBCNKJ6ywn4QvG4fGtU4xbubuYEFOuWEOSqgM-yldbiYi-8PAgq84ZxZfY01vIJViEV1YzJX7tG06wJBioCbvRom1rq5yd3AjyZBDhhoH-AyUfAhB21Jtic-X-dv6-XaKOusBAzzQYSpmdxvvKrrYQtLAyjpt7ixOT1DZLurl9cUlT22C6PeNHL5YyHp1EL08AxCAQjgKS9PsHwCEDpI-ui3u6hCpueY9W3ktOd0kpXHOXp-y2cdN_cWx_c_wXk7pUhioP8NF3LfWMWvOZengwzJTpDoSONk7CdU9Fe8T8b97jVMMpfdWPOcUGnPFoJ_TF0iNgf4-hV1AgAPzvL0P1lqTEf6zHf6EPhuxhEMcqcw3chNwGUIqHe9vFZoidyXc4GOn7GLOgnEv0zjmCiga9BE7fL3S1KmWfCLkBho6lEr_u5cyHEs0JOQNTye6euk5DXlL6qzfaN9xqx30C4tkhfDI8fPPEVp4xpSH-59m88R6CylgGUcOtZ1gtMJHQNeKwYjoFQW8fGzK5JKdgkud33MC-KTjkhA-Yc55yNI-ZqrLgmi19mNNN56fW7k1Qo6pqrPwlS7r4Fia5XjBUotc8otu2eg9jiwBf47RuMZ7GxZDFFjm9DcTzCqvbvyQjvhnUKAKspCi404iAkugjUB7d5BGlcz0o1KBsHU2cqqmkSEYZtR-cv2i5flExjvHPrwBHfOc5OryBqqbfANlOrAnzSUFXNq_MQFwSJn_PdX-jz5vtqNECbQe3YElTzO7IKRJlEiADOeNcjpz0M717P5SmqLUOuo3ysQTFBn_X-mE73nixbE-zf9NnZCq9DtXH2z4NBSmutrq-xdbW88nYkYWRGBTOFVlQinp6QBUQkFdhBQIlIC3B_4_ZZPYUkMQDQXYDTwrxcAT4SidmM9g-QwWLZuu5Wos4tXAPpqJpzYe4AuLqx4oaauDud1FvCAj-o2JzWlHYhk1HJrN0vU0d73dWQkQbKmmecUd39Tbab5j1FZyyj2kTChCJzg98yaOOT47SeRq7Kt18Qsuqd4gNwIpwQLRkmZHx8aojT_ivHVF5dZRO53rvpusfvyOIszwN7G_qTLzTVKnVDH5aHKbAIwyKF_2Urg-pybmjbUXyp5juZOo5TbGEMIaYJZlbjZwKovIbTfAcNiGC577_6NAf_hvkT_h2eRpXZmAYMLc24lvZalx4GDWzLR9rURI-fXMQTX_RfVeoWbGWDQQsewqXRn1nl7TP36NWGmDyEYZAodkODkp9BYxycLl3TQw9MpItq-jAOAWgNotsa3SNrQ6y46othZyci--JoqKp6RknLuvhsVpsLO7l-k270KjVRO2-2zd-Ailg4IkMZBo9iBa5nDQWyCbZ44JPrpWPbSbhBTXaOcKqQ3Bq3SUCSa4sj4HzbOs-VElEzj2vyg_sIDlb3nutOIwsaW613O6Jvs3C1y_oaLF7iY0N2-oEmhGGM4KkS3HVnsX8mUa_yejBnghsbpoCvQTdCid_uO_VnuEIR7mCxwO4m0iNE2P0Mu-Ss9oG9OJDXVVaugKgmBxJ8Q_M19ceQJ8Tm2GD8CIJo_hAVqUIPvXyaJB_1QqTvZSxD_gC3c7qqVYIox7N32xWRr4bO9AWD2dYuLGTeZi.Euc2_dY6btWFIA45W3HTAA'

#session_api = pyChatGPT.ChatGPT(session_token=session_token)

token = 'MTAwNzU2OTQxMDc0NTE3MjAxOQ.GmjeuU.14Q15nHPvinQx0VmQ0V5fJs58oj6B78nZ6OJlM'


class BandoMod(ui.Modal, title='Bando staff'):
    nome = ui.TextInput(label='Nome', placeholder='Inserisci il tuo nome', style=discord.TextStyle.short, max_length=30)
    eta = ui.TextInput(label='Età', placeholder='Inserisci la tua età', style=discord.TextStyle.short, max_length=6)
    ruolo = ui.TextInput(label='Per quale ruolo ti candidi?', placeholder='(Grafico, Developer, Moderatore...)',
                         style=discord.TextStyle.short, max_length=20)
    motivo = ui.TextInput(label='Perchè vuoi candidarti da noi?', placeholder='Voglio candidarmi perchè ...',
                          style=discord.TextStyle.long, max_length=250)

    async def on_submit(self, interaction: discord.Interaction):
        emb = discord.Embed(title='Bando Mod',
                            description=f'**{self.nome.label}**\n {self.nome}\n\n **{self.eta.label}**\n {self.eta}\n\n **{self.ruolo.label}** \n {self.ruolo} \n\n**{self.motivo.label}**\n {self.motivo}',
                            color=discord.Color.from_rgb(255, 0, 0))
        emb.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=emb)
        async for message in interaction.channel.history():
            if not message.embeds:
                continue
            if message.embeds[0].title == emb.title and message.embeds[0].colour == emb.colour:
                msg = message
                break
            else:
                return
        await msg.add_reaction('waiting:1081505862687936522')
        await interaction.user.send(
            'Grazie di aver mandato la tua richiesta! Verrà presto controllata da uno staffer che ti contatterà.')


class Embed(ui.Modal, title='Embed Builder'):
    title = ui.TextInput(label='Titolo', placeholder='Inserisci il titolo', style=discord.TextStyle.short,
                         max_length=30)
    description = ui.TextInput(label='Corpo del testo', placeholder='Inserisci il corpo del testo',
                               style=discord.TextStyle.paragraph, max_length=240)
    color = ui.TextInput(label='Colore', placeholder='Inserisci il colore', style=discord.TextStyle.short,
                         max_length=30)
    author = ui.TextInput(label='Autore', placeholder='Inserisci l\'id dell\'autore (senza discriminatore)',
                          style=discord.TextStyle.short, max_length=30)
    channel = ui.TextInput(label='Canale', placeholder='Inserisci l\'id del canale in cui mandare l\'embed',
                           style=discord.TextStyle.short, max_length=20)

    async def on_submit(self, interaction: discord.Interaction):
        emb_channel = bot.get_channel(self.channel)
        emb_author = bot.get_user(self.author)
        emb = discord.Embed(title=self.title, description=self.description,
                            color=discord.Color.from_str(matplotlib.colors.cnames[str(self.color)]))
        emb.set_author(name=emb_author, icon_url=emb_author.avatar.url)
        await interaction.response.send_message('Mandato', ephemeral=True, delete_after=1)
        await emb_channel.send(embed=emb)


class Client(commands.Bot):

    def __init__(self):
        intents = discord.Intents().all()
        super().__init__(command_prefix=commands.when_mentioned_or('!'), intents=intents)
        self.antispam = commands.CooldownMapping.from_cooldown(10, 20, commands.BucketType.member)
        self.too_many_violations = commands.CooldownMapping.from_cooldown(3, 60, commands.BucketType.member)
        self.bad_words = ['macteo', 'stronzo', 'coglione', 'porcodio', 'mactesito', 'cojon', 'sburra', 'sborra',
                          'vivalafiga', 'minchia']
        

    @bot.event
    async def on_ready(self):
        print('Il bot è online')
        try:
            synced = await bot.tree.sync()
            print(f'Comandi sincronizzati: {len(synced)}')
            await bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name=f' 💡| {len(bot.guilds)} server'))
            db = sqlite3.connect('warns.db')
            c = db.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS warns(user INTEGER, reason TEXT, time INTEGER, guild INTEGER);')
            db.commit()
            db.close()
        except Exception as e:
            print(str(e))

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
                try:
                    await message.author.send(f'{message.author.name}, sei stato mutato in {message.guild.name}')
                except:
                    pass

    @bot.event
    async def on_message(self, message):
        if any(n in message.content for n in self.bad_words):
            await message.delete()
            await message.author.timeout(timedelta(0, 0, 1, 0))
            await message.channel.send(f'{message.author.mention}, non puoi scrivere quella parola!')

    @bot.event
    async def on_member_ban(self, guild, member):
        with open('bans.txt', 'a+') as f:
            f.write(f'{member.name} in {guild.name}')

    @bot.event
    async def on_member_kick(self, guild, member):
        with open('kicks.txt', 'a+') as f:
            f.write(f'{member.name} in {guild.name}')

    @bot.event
    async def on_reaction_add(self, reaction, user):
        if reaction.message.channel == bot.get_channel(1057653487632130058):
            if str(reaction.emoji) == 'accepted:1077015164978733176' or str(reaction.emoji) == 'rejected:1077016217736454194':
                reaction.remove(bot)
            elif str(reaction.emoji) == 'waiting:1081505862687936522':
                return
            else:
                return

    async def setup_hook(self) -> None:
        self.add_view(view())
        self.add_view(view2())
        self.add_view(ticket())




bot = Client()
bot.remove_command('help')


async def addwarn(interaction: discord.Interaction, user, reason):
    db = sqlite3.connect('warns.db')
    c = db.cursor()
    c.execute('INSERT INTO warns (user, reason, time, guild) VALUES (?, ?, ?, ?);',
              (user.id, reason, datetime.now().timestamp(), interaction.guild.id))
    db.commit()
    db.close()

async def count_update():
    channel_members = await bot.get_channel(1075472059599159306)
    channel_users = await bot.get_channel(1075472063663439903)
    channel_bots = await bot.get_channel(1075472068017127474)
    members = []
    async for guild in bot.guilds:
        async for member in guild.members:
            yield member
            members.append(member.name)
    users = []
    async for guild in bot.guilds:
        async for member in guild.members:
            yield member
            if not member.bot:
                users.append(member.name)
    bots = []
    async for guild in bot.guilds:
        async for member in guild.members:
            yield member
            if member.bot:
                bots.append(member.name)
    await channel_members.edit(name=f'ᴍᴇᴍʙᴇʀ: {len(members)}')
    print(len(members))
    await channel_users.edit(name=f'ᴜꜱᴇʀ: {len(users)}')
    print(len(users))
    await channel_bots.edit(name=f'ʙᴏᴛ: {len(bots)}')
    print(len(bots))


class view(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Invia', style=discord.ButtonStyle.green, custom_id='1')
    async def callback(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_modal(BandoMod())


class view2(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Ottieni', style=discord.ButtonStyle.blurple, custom_id='2')
    async def callback(self, interaction: discord.Interaction, Button: discord.ui.Button):
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

    @discord.ui.button(label='Ticket', style=discord.ButtonStyle.blurple, custom_id='3')
    async def callback(self, interaction: discord.Interaction, Button: discord.ui.Button):
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(f'Non puoi usare questo botton per altri {round(retry, 1)}',
                                                           ephemeral=True)
        guild = bot.get_guild(1043217543604748290)
        modrole = discord.utils.get(guild.roles, id=1046907122627133521)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            modrole: discord.PermissionOverwrite(read_messages=True)}
        with open('tickets.txt', 'r+') as f:
            line_count = 0
            f.write('ticket\n')
            for line in f:
                line_count += 1
        channel = await interaction.guild.create_text_channel(name=f'{interaction.user.name} ({line_count})',
                                                              overwrites=overwrites)
        controller = ui.View()
        btnclose = ui.Button(label='Chiudi Ticket', style=discord.ButtonStyle.danger, custom_id='6')

        async def callback(interaction: discord.Interaction):
            await channel.delete()
            await interaction.response.send_message('Cancellato', ephemeral=True, delete_after=1)

        btnclose.callback = callback
        controller.add_item(btnclose)
        await channel.send(f'Il ticket {channel.name} è stato creato', view=controller)
        await interaction.response.send_message(f'Il canale {interaction.user.name} è stato creato', ephemeral=True)


@bot.tree.context_menu(name='Informazioni')
async def identità(interaction: discord.Interaction, member: discord.Member):
    try:
        emb = discord.Embed(title=f'{member.name}', description=f'Ecco alcune informazioni su {member.mention}.',
                            color=discord.Color.from_rgb(0, 0, 255))
        emb.add_field(name='Id', value=member.id, inline=False)
        emb.add_field(name='Su discord da:', value=member.created_at.strftime("Il %d %h %Y alle %H:%M:%S"),
                      inline=False)
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
async def autorole(interaction: discord.Interaction):
    emb = discord.Embed(title='Ruolo FiveM',
                        description='Clicca il bottone qui sotto per ricevere il ruolo ed accedere alla categoria di FiveM')
    await interaction.response.send_message('Mandato!', ephemeral=True, delete_after=1)
    await interaction.channel.send(embed=emb, view=view2())


@bot.tree.command(name='tickettake', description='Manda il ticket')
async def tickettake(interaction: discord.Interaction):
    emb = discord.Embed(title='Ticket',
                        description='Hai bisogno di assistenza?\n Clicca il bottone qui sotto per creare un ticket',
                        color=discord.Color.from_rgb(0, 0, 255))
    await interaction.response.send_message('Mandato!', ephemeral=True, delete_after=1)
    await interaction.channel.send(embed=emb, view=ticket())


@bot.tree.command(name='bandomod', description='Manda il bando per mod')
async def bandomod(interaction: discord.Interaction):
    emb = discord.Embed(title='Bando Mod', description='Clicca il bottone qui sotto per inviare il tuo bando')
    await interaction.response.send_message('Mandato', ephemeral=True, delete_after=1)
    await interaction.channel.send(embed=emb, view=view())


@bot.tree.command(name='banhistory', description='Visualizza la storia dei ban e delle espulsioni di un membro')
@app_commands.describe(member='Membro da controllare')
async def banhistory(interaction: discord.Interaction, member: discord.Member):
    bans = []
    kicks = []
    fb = open('bans.txt', 'r').read()
    fk = open('kicks.txt', 'r').read()
    linesb = fb.readlines()
    linesk = fk.readlines()
    for line in linesb:
        if member.name in line and interaction.guild.name in line:
            bans.append(member.name)
    for linek in linesk:
        if member.name in linek and interaction.guild.name in line:
            kicks.append(member.name)
    emb = discord.Embed(title=f'{member.name}',
                        description=f'{member.mention}\n\n Bans: {len(bans)}\n\n Kick: {len(kicks)}',
                        color=discord.Color.red)
    emb.set_author(name=member.name, icon_url=member.avatar.url)
    await interaction.response.send_message(embed=emb)


@bot.tree.command(name='roll', description='Scegli un numero casuale')
@app_commands.describe(min='Il numero minimo possibile', max='Il numero massimo possibile')
async def roll(interaction: discord.Interaction, min: int, max: int):
    emb = discord.Embed(title='Numero casuale', description=f'**{random.randint(min, max)}**')
    await interaction.response.send_message(embed=emb)


@bot.tree.command(name='kick', description='Espelli un membro')
@app_commands.describe(member='Membro da espellere', reason='Motivo dell\'espulsione')
async def kick(interaction: discord.Interaction, member: discord.Member, reason:str):
    emb = discord.Embed(title='Membro espulso', description=f'{member.name} è stato espulso',
                        color=discord.Color.from_rgb(255, 0, 0))
    await interaction.response.send_message(embed=emb)
    await member.kick(reason=reason)


@bot.tree.context_menu(name='Espelli')
async def kick(interaction: discord.Interaction, member: discord.Member):
    emb = discord.Embed(title='Membro espulso', description=f'{member.name} è stato espulso',
                        color=discord.Color.from_rgb(255, 0, 0))
    await interaction.response.send_message(embed=emb)
    await member.kick()


@bot.tree.command(name='ban', description='Banna un utente')
@app_commands.describe(member='Membro da bannare', reason='Motivo')
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str):
    emb = discord.Embed(title=f'{member.name} è stato bannato', description=f'{member.mention} è stato bannato',
                        color=discord.Color.from_rgb(255, 0, 0))
    emb.add_field(name='Motivo:', value=f'{reason}')
    await interaction.response.send_message(embed=emb)
    await member.ban(reason=reason)


@bot.tree.context_menu(name='Banna')
async def ban(interaction: discord.Interaction, member: discord.Member):
    emb = discord.Embed(title=f'{member.name} è stato bannato', description=f'{member.mention} è stato bannato',
                        color=discord.Color.from_rgb(255, 0, 0))
    await interaction.response.send_message(embed=emb)
    await member.ban()


@bot.tree.command(name='warn', description='Warna un utente')
@app_commands.describe(member='Membro da warnare', reason='Motivo del warn')
async def warn(interaction: discord.Interaction, member: discord.Member, reason: str = 'Nessun motivo previsto'):
    await addwarn(interaction, member, reason)
    emb = discord.Embed(title='Membro warnato',
                        description=f'{member.mention} è stato warnato da {interaction.user} per {reason}',
                        colour=discord.Colour.from_rgb(255, 0, 0))
    await interaction.response.send_message(embed=emb)
    db = sqlite3.connect('warns.db')
    c = db.cursor()
    c.execute('SELECT reason FROM warns WHERE user = (?) AND guild = (?)', (member.id, interaction.guild.id))
    data = c.fetchone()
    if len(data) > 3:
        emb = discord.Embed(title='Membro bannato',
                            description=f'{member.mention} ha raggiunto 4 warns ed è stato bannato.',
                            color=discord.Color.from_rgb(255, 0, 0))
        await interaction.channel.send(embed=emb)
        await member.ban()


@bot.tree.command(name='unwarn', description='Warna un utente')
@app_commands.describe(member='Membro da unwarnare')
async def unwarn(interaction: discord.Interaction, member: discord.Member):
    db = sqlite3.connect('warns.db')
    c = db.cursor()
    c.execute('SELECT reason FROM warns WHERE user = (?) AND guild = (?)', (member.id, interaction.guild.id))
    data = c.fetchone()
    if data:
        c.execute('DELETE FROM warns WHERE user = (?) AND guild = (?)', (member.id, interaction.guild.id))
        emb = discord.Embed(title='Membro warnato',
                            description=f'{member.mention} è stato unwarnato da {interaction.user}',
                            colour=discord.Colour.from_rgb(0, 128, 0))
        await interaction.response.send_message(embed=emb)
    else:
        await interaction.response.send_message('Il membro non ha warn.')
    db.commit();
    db.close()


@bot.tree.command(name='warnings', description='Controlla i warn di un membro')
@app_commands.describe(member='Il membro da controllare')
async def warnings(interaction: discord.Interaction, member: discord.Member):
    conn = sqlite3.connect('warns.db')
    c = conn.cursor()
    c.execute('SELECT * FROM warns WHERE user = (?) AND guild = (?)', (member.id, interaction.guild.id))
    warns = c.fetchall()
    emb = discord.Embed(title=f'Warns di {member.name}', description=f'{member.mention} ha {len(warns)} warn')
    await interaction.response.send_message(embed=emb)


@bot.tree.command(name='say', description='Fai dire qualcosa al bot')
@app_commands.describe(messaggio='Fai scrivere qualcosa al bot')
async def say(interaction: discord.Interaction, messaggio: str):
    await interaction.response.send_message('Mandato!', ephemeral=True, delete_after=1)
    await interaction.channel.send(messaggio)


@bot.tree.command(name='avatar', description='Manda l\'avatar di un membro')
@app_commands.describe(member='Membro da taggare con il suo embed')
async def avatar(interaction: discord.Interaction, member: discord.Member):
    Embed = discord.Embed(title=member.mention, color=discord.Color.from_rgb(0, 0, 255))
    Embed.set_image(url='{}'.format(member.avatar.url))
    btn = ui.Button(label='Download avatar', style=discord.ButtonStyle.url, url=member.avatar.url)
    view = ui.View()
    view.add_item(btn)
    await interaction.response.send_message(embed=Embed, view=view)


@bot.tree.command(name='clear', description='Pulisce la chat')
@app_commands.describe(amount='Numero di messaggi da eliminare')
async def clear(interaction: discord.Interaction, amount: int = None):
    await interaction.response.defer()
    if amount == None:
        await interaction.response.send_message(f'Sono stati cancellati {amount} messaggi', ephemeral=True)
        await interaction.channel.purge(limit=1000000)
    else:
        try:
            int(amount)
        except:
            await interaction.response.send_message('Per favore inserisci un numero valido(max 1000000).',
                                                    ephemeral=True)
        else:
            await interaction.channel.purge(limit=amount)
            await asyncio.sleep(1)
            await interaction.response.send_message(f'Sono stati cancellati {amount} messaggi', ephemeral=True)

@bot.tree.command(name='mute', description='Muta un utente')
@app_commands.describe(member='membro', days='giorni', hours='ore', minutes='minuti', seconds='secondi',
                       reason='motivo')
async def mute(interaction: discord.Interaction, member: discord.Member, days: int = 0, hours: int = 0,
               minutes: int = 0, seconds: int = 0, reason: str = None):
    tempo = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    await member.timeout(tempo, reason=reason)
    temponew = f'{days} : {hours} : {minutes} : {seconds}'
    if reason:
        emb = discord.Embed(title='Membro mutato',
                            description=f'{interaction.user.mention} ha mutato {member.mention} per {temponew} per {reason}',
                            color=discord.Color.from_rgb(255, 0, 0))
    elif not reason and days or hours or minutes or seconds:
        emb = discord.Embed(title='Membro mutato',
                            description=f'{interaction.user.mention} ha mutato {member.mention} per {temponew}',
                            color=discord.Color.from_rgb(255, 0, 0))
    elif not reason and not days and not hours and not minutes and not seconds:
        emb = discord.Embed(title='Membro mutato', description=f'Specifica un tempo',
                            color=discord.Color.from_rgb(255, 0, 0))
    else:
        print('Errore')
    await interaction.response.send_message(embed=emb)


@bot.tree.command(name='ismuted', description='Controlla se il membro è mutato')
@app_commands.describe(member='membro')
async def ismuted(interaction: discord.Interaction, member: discord.Member):
    if member.is_timed_out:
        emb = discord.Embed(title=f'{member.name} è mutato')
        await interaction.response.send_message(embed=emb)
    elif member.is_timed_out:
        emb = discord.Embed(title=f'{member.name} non è mutato')
        await interaction.response.send_message(embed=emb)
    else:
        emb = discord.Embed(title=f'{member.name} non esiste')
        await interaction.response.send_message(embed=emb)


@bot.tree.command(name='embed', description='Crea un embed')
@app_commands.choices(colour=[discord.app_commands.Choice(name='red', value=1),
                              discord.app_commands.Choice(name='blue', value=2),
                              discord.app_commands.Choice(name='green', value=3),
                              discord.app_commands.Choice(name='darkblue', value=4),
                              discord.app_commands.Choice(name='white', value=5),
                              discord.app_commands.Choice(name='darkgreen', value=6),
                              discord.app_commands.Choice(name='darkgrey', value=7),
                              discord.app_commands.Choice(name='darkmagenta', value=8),
                              discord.app_commands.Choice(name='darkpurple', value=9),
                              discord.app_commands.Choice(name='darkred', value=10),
                              discord.app_commands.Choice(name='violet', value=11),
                              discord.app_commands.Choice(name='grey', value=12),
                              discord.app_commands.Choice(name='lightgrey', value=13),
                              discord.app_commands.Choice(name='magenta', value=14),
                              discord.app_commands.Choice(name='orange', value=15),
                              discord.app_commands.Choice(name='purple', value=16),
                              discord.app_commands.Choice(name='teal', value=17),
                              discord.app_commands.Choice(name='yellow', value=18)]
                      )
@app_commands.describe(title='Il titolo dell\'embed', description='Il corpo dell\'embed (\\n per andare a capo)',
                       url='Url dell\'embed', author='Autore dell\'embed (appare in alto a sinistra)',
                       footer='Footer dell\'embed', colour='Colore dell\'embed',
                       preview='Mandare l\'embed in preview? (solo tu puoi vedrlo)')
async def embed(interaction: discord.Interaction, title: str, description: str, url: str = None,
                author: discord.Member = None, footer: str = None, preview: bool = False,
                colour: discord.app_commands.Choice[int] = None):
    if preview:
        colour = str(colour.name)
        btn = ui.Button(label='Manda Embed', style=discord.ButtonStyle.green)

        async def callback(interaction: discord.Interaction):
            await interaction.response.send_message('Embed mandato', ephemeral=True, delete_after=1)
            await interaction.channel.send(embed=emb)

        btn.callback = callback
        view = ui.View()
        view.add_item(btn)
        emb = discord.Embed(title=title, description=description, url=url,
                            colour=discord.Color.from_str(matplotlib.colors.cnames[colour]))
        emb.set_author(name=author, icon_url=author.avatar.url)
        emb.set_footer(text=footer)
        await interaction.response.send_message(embed=emb, view=view, ephemeral=True)
    if not preview:
        colour = str(colour.name)
        embn = discord.Embed(title=title, description=description, url=url,
                             colour=discord.Color.from_str(matplotlib.colors.cnames[colour]))
        embn.set_author(name=author, icon_url=author.avatar.url)
        embn.set_footer(text=footer)
        await interaction.response.send_message('Embed mandato', ephemeral=True, delete_after=1)
        await interaction.channel.send(embed=embn)


@bot.tree.command(name='nick', description='Modifica il nickname in questo server')
@app_commands.describe(nick='Il tuo nuobo nickname')
async def nick(interaction: discord.Interaction, nick: str):
    try:
        await interaction.user.edit(nick=nick)
        emb = discord.Embed(title='Nickname cambiato',
                            description=f'Il nickname di {interaction.user.mention} è stato cambiato in {interaction.user.nick}.',
                            color=discord.Color.red)
        await interaction.response.send_message(embed=emb)
    except discord.Forbidden:
        await interaction.response.send_message('Mi dispiace, ma non ho il permesso per cambiarti il nome.')


@bot.tree.command(name='giveaway', description='Fai un giveaway')
@app_commands.describe(name='Nome del giveaway')
async def giveaway(interaction: discord.Interaction, name: str):
    memberlist = [member for member in interaction.guild.members if not member.bot and member != interaction.user]
    winner = random.choice(memberlist).mention
    emb = discord.Embed(title=f'Giveaway: {name}', description=f'{winner} ha vinto il giveaway!', colour=discord.Colour.from_rgb(0,0,255))
    await interaction.response.send_message(embed=emb)


@bot.tree.command(name='help', description='Aiuto')
async def help(interaction: discord.Interaction):
    emb = discord.Embed(
        title='Help',
        description=
        """\n**/say:** Fai dire qualcosa al bot.\n\n **/avatar {member}:** Ottieni l\'avatar del membro.\n\n **/ban {member}:** Banna un membro.\n\n **/kick {member}:** Espelle un membro.\n\n **/clear {amount}:** Pulisce la chat.\n\n **/roll {min} {max}:** Estrae un numero casuale tra due numeri dati.\n\n **/mute {member} {time}:** Muta un membro per il tempo dato.\n\n **/unmute {member}:** Smuta un membro.\n\n **/warn {member} {reason}:** Warna un membro per una ragione.\n\n **/unwarn {member}:** Unwarna un membro.\n\n
         **/warnings {member}:** Controlla i warnings di un membro\n\n **/nick {nickname}:** Cambia il tuo nickname.\n\n
         **/embed {title} {description} {author} {colour} {footer} {url} {preview}:** Crea un embed personalizzato.\n\n
         **/tickettake:** Ottieni il ticket.\n\n **/banhistory {member}:** Controlla se il membro è stato bannato/espulso.\n\n
         **/giveaway {name}:** Fai un giveaway.\n\n""",
        color=discord.Color.from_rgb(0, 0, 255))
    view = ui.View()
    btn = ui.Button(label='➡️', style=discord.ButtonStyle.blurple, custom_id='8')

    async def callback(interaction: discord.Interaction):
        emb2 = discord.Embed(
            title='Help - Page 2',
            description=
            '\n**Banna(context_menu):** Banna un membro\n\n **Espelli(context_menu):** Espelle un membro\n\n **Informazioni(context_menu):** Informazioni sul membro\n\n **Avatar(context_menu):** Ottieni l\'avatar del membro.\n\n'

        )
        await interaction.response.edit_message(embed=emb2)

    btn.callback = callback

    btn2 = ui.Button(label='⬅️',
                     style=discord.ButtonStyle.blurple,
                     custom_id='9')

    async def callback2(interaction: discord.Interaction):
        await interaction.response.edit_message(embed=emb)

    btn2.callback = callback2
    view.add_item(btn)
    view.add_item(btn2)
    await interaction.response.send_message(embed=emb, view=view)

@bot.tree.command(name='counter_update', description='Forza l\' aggiornamento del contatore')
async def counter_update(interaction:discord.Interaction):
    await count_update()
    await interaction.response.send_message('Contatore dei membri ricaricato!')

@bot.tree.command(name='unban', description='Unbanna un membro precedentemente bannato')
@app_commands.describe(user='Utente da unbannare')
async def unban(interaction:discord.Interaction, user:str):
    userunb = await commands.converter.UserConverter().convert(interaction, user)
    bans = tuple(ban_entry.user for ban_entry in await interaction.guild.bans())
    if user in bans:
        await interaction.guild.unban(userunb)
    emb = discord.Embed(title='Membro unbannato', description=f'{discord.Member(userunb).mention} è stato unbannato da {interaction.user}')
    await interaction.response.send_message(embed=emb)

@bot.tree.command(name='poll', description='Crea un sondaggio')
@app_commands.describe(question='La domanda da chiedere', option_1='Prima opzione', option_2='Seconda opzione', time='Durata del sondaggio')
async def poll(interaction:discord.Interaction, question:str, option_1:str, option_2:str, time:int):
    time = time.split(':')
    if len(time) == 1:
        timew = timedelta(seconds=time[0])
    elif len(time) == 2:
        timew = timedelta(minutes=time[0], seconds=time[1])
    elif len(time) == 3:
        timew = timedelta(hours=time[0], minutes=time[1], seconds=time[2])
    elif len(time) == 3:
        timew = timedelta(days=time[0], hours=time[1], minutes=time[2], seconds=time[3])
    else:
        await interaction.response.send_message(f'{str(time)} non è supportato! Inserisci al massimo 7 giorni.')
    conn = sqlite3.connect('polls.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS polls(question TEXT, option_1 INTEGER, option_2 INTEGER, time INTEGER)')
    cur.execute('INSERT IF NOT EXISTS IN polls(?, ?, ?, ?)', (question, 0, 0, time))
    cur.execute('SELECT option_1 FROM polls')
    votes1 = cur.fetchone()
    cur.execute('SELECT option_2 FROM polls')
    votes2 = cur.fetchone()
    cur.execute('SELECT time FROM polls')
    time = cur.fetchone()
    emb = discord.Embed(title=f'{question}', description='\n', color=discord.Color.from_rgb(255,0,0))
    emb.add_field(name='Opzione 1: ', value='50%')
    emb.add_field(name='Opzione 2: ', value='50%')
    emb.add_field(name='Tempo rimanente: ', value=str(timew))
    emb.set_footer(text=f'Sondaggio di {interaction.user}', icon_url=interaction.user.avatar.url)
    btn = ui.Button(label=option_1, style=discord.ButtonStyle.blurple, emoji='1️⃣')
    async def callback(interaction:discord.Interaction):
        cur.execute('SET option_1 FROM polls = option_1 + 1')
        cur.execute('SELECT option_1 FROM polls')
        votes1 = cur.fetchone()
        cur.execute('SELECT option_2 FROM polls')
        votes2 = cur.fetchone()
        perc1 = votes1/(votes1 + votes2) * 100
        emb.add_field(name=f'{option_1}:', value=f'{str(perc1)}')
        await interaction.response.edit_message(embed=emb)
    btn.callback = callback
    btn1 = ui.Button(label=option_1, style=discord.ButtonStyle.blurple, emoji='2️⃣')
    async def callback2(interaction:discord.Interaction):
        cur.execute('SET option_2 FROM polls = option2 + 1')
        cur.execute('SELECT option_2 FROM polls')
        votes2 = cur.fetchone()
        cur.execute('SELECT option_1 FROM polls')
        votes1 = cur.fetchone()
        perc2 = votes2/(votes1 + votes2) * 100
        emb.add_field(name=f'{option_1}:', value=f'{str(perc2)}')
        await interaction.response.edit_message(embed=emb)
    btn1.callback = callback2
    view = ui.View()
    view.add_item(btn)
    view.add_item(btn1)
    await interaction.response.send_message(embed=emb, view=view)
    conn.commit()
    conn.close()

# keep_alive()
bot.run(token)
schedule.every().minute.do(count_update)
