import discord
import datetime

client = discord.Client()

today = datetime.date.today()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '$list':
        await message.channel.send(today)
        await message.channel.send('今日も元気に交流戦いけぜ！')
        await message.channel.send('20@6\n21@6\n22@6\n23@6\n24@6\n25@6')



client.run(str(os.environ.get('BOT_TOKEN')))
