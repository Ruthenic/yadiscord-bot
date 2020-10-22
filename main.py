import discord
import random
import traceback
import os
import operator
import array as arr
from string import ascii_letters as preletters
from datetime import datetime

letters = [letter for letter in preletters]
prefix = '!/'

def log_message(user_message, sent_message): #log commands and their replies
    #reference go brrrr
    print(f'\nMessage hazbin sent in response to \'user_message.content\'\nResponse: {sent_message}\nUser: {user_message.author}, UserID: {user_message.author.id}\nGuild: {user_message.guild.name}\nChannel: {user_message.channel.name}') # onboho says hi again :)
class MyClient(discord.Client):
    async def on_ready(self): 
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return #dont reply to ourselves
        try:
            if message.content == prefix + 'ping':
                guild_name = discord.Guild.name
                sent_message = 'Pinging...'
                bot_message = await message.channel.send(sent_message)
                await bot_message.edit(content=f"Pong! {round(((datetime.timestamp(bot_message.created_at)-datetime.timestamp(message.created_at))%1)*1000)}ms") 
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'say'):
                saying = message.content.replace(prefix + 'say ', "")
                await message.channel.send(saying)
                log_message(message, saying)
            if message.content.startswith(prefix + 'range'):
                range_string = message.content.replace(prefix + 'range ', "")
                range1 = range_string.partition(',')[0].replace(',', '')
                range2 = range_string.partition(',')[2].replace(',', '')
                print(range1, range2)
                sent_message = str(random.randrange(int(range1), int(range2)))
                await message.channel.send(sent_message)
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'math'):
                math_string = message.content.replace(prefix + 'math ', "")
                if any(ext in math_string for ext in letters):
                    await message.channel.send("lmao did you just try to execute something with a letter in an eval statement? nonono, you cannnot do that")
                else:
                    #sent_message = str(eval(math_string))
                    sent_message = "Removed math function due to ability to crash python, and therefore the bot, with a large enough exponential equasion. Sorry for the inconvience - Man Behind the Machine"
                    await message.channel.send(sent_message)
                    log_message(message, sent_message)
            if message.content.startswith(prefix + 'eval'):
                if message.author.id == "680959829426438168":
                	guild_name = discord.Guild.name
                	sent_message = eval(message.content.replace(prefix + 'eval ', ""))
                	await message.channel.send(sent_message)
                	log_message(message, sent_message)
                else:
                    guild_name = discord.Guild.name
                    sent_message = "haha you\'re not the owner of the bot so you cant use it"
                    await message.channel.send(sent_message)
                    log_message(message, sent_message)
                
                
        except Exception as e:
            await message.channel.send(f"lol an error happened get cucked by the python code loser\nTraceback: {str(e)}") #lol
            print(e)
try:
    botid = os.environ["BOTID"] #try to use heroku config var to get botID
except: 
    print("Running on local machine. Using text file...") #if config var not found, utilize botid.txt for bot id
    try:
        botid = open (r'botid.txt', "r")
        botid = botid.read() #read botID back into the var
    except:
        print("Please place valid bot ID in botid.txt beside main.py")
client = MyClient()
client.run(botid) #run with found botID
