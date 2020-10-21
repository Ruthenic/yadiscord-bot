import discord
import random
import traceback
import os

prefix = '!/'
def log_message(command, sent_message):
    print('Message sent in response to \'' + command + '\': ' + sent_message)
cid = 0
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        try:
            if message.content == prefix + 'ping':
                guild_name = discord.Guild.name
                sent_message = 'Pong!'
                await message.channel.send(sent_message)
                log_message(message.content, sent_message)
            if message.content.startswith(prefix + 'say'):
                saying = message.content.replace(prefix + 'say ', "")
                await message.channel.send(saying)
                log_message(message.content, saying)
            if message.content.startswith(prefix + 'range'):
                range_string = message.content.replace(prefix + 'range ', "")
                range1 = range_string.partition(',')[0].replace(',', '')
                range2 = range_string.partition(',')[2].replace(',', '')
                print(range1, range2)
                sent_message = str(random.randrange(int(range1), int(range2)))
                await message.channel.send(sent_message)
                log_message(message.content, sent_message)
        except Exception as e:
            await message.channel.send("lol an error occured get cucked by the python code loser")
            await message.channel.send("traceback: " + e) 
            print(e)
    async def send_message(message, command):
        channel = await client.get_channel(cid)
        await channel.send(command.replace('say ', ''))
        print('Message \'' + command.replace('say ', '') + '\' hasbeen sent to ' + message.channel.id)

try:
    botid = os.environ["BOTID"]
except: 
    print("Running on local machine. Using text file...")
    try:
        botid = open (r'botid.txt', "r")
        botid = botid.read()
    except:
        print("Please place valid bot ID in botid.txt beside main.py")
client = MyClient()
client.run(botid)
