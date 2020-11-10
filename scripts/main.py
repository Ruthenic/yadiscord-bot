import discord
import random
import traceback
import os
import operator
import array as arr
import time
from datetime import datetime
from translate import Translator

#import firebase_admin
#from firebase_admin import credentials,firestore

#revive code if i use a database ever
#cred = credentials.Certificate('database-key.json')
#firebase_admin.initialize_app(cred)
#db = firestore.client()
#servers_ref = db.collection(u"servers")
credits = " People who've contributed: \nRuthenic (Drake),\ntestersbastarps (onboho),\nGnog3 (Gnog3)"
help_message = 'YaDiscord Bot\'s commands:\n`!/help` Show the command list.\n`!/credits` Basically credits.\n`!/ping` Ping the bot.\n`!/owo` Print a random OwO/UwU\n`!/say (text)` Make the bot say something.\n`!/range (first-number), (second-number)` Make the bot generate a random number in given range.\n`!/math (math-stuff)` Do simple math\n`!/eval` Evalutate something. Owner only.' #very long string, i know. do i care? no
prefix = '!/'
owo = ['owo', 'OwO', 'oWo', 'OWO', 'uwu', 'UwU', 'uWu', 'UWU'] #owo

def log_message(user_message, sent_message): #log commands and their replies
    #reference go brrrr
    print(f'\nMessage hazbin sent in response to \'{user_message.content}\'\nResponse: {sent_message}\nUser: {user_message.author}, UserID: {user_message.author.id}\nGuild: {user_message.guild.name}, GuildID: {user_message.guild.id}\nChannel: {user_message.channel.name}, ChannelID:{user_message.channel.id}') # onboho says hi again :)  
        
class MyClient(discord.Client):
    async def on_ready(self): 
        print('Logged in as', self.user)

    async def on_message(self, message):
        if str(message.author.id) == '750362382584512623':
            return #dont reply to the normal version of the bot
        if str(message.author.id) == '768549646720172042':
            return #dont reply to the bleeding edge version of the bot
        try:
            if message.content == prefix + 'ping':
                guild_name = discord.Guild.name
                sent_message = 'Pinging...'
                bot_message = await message.channel.send(sent_message)
                await bot_message.edit(content=f"Pong! {round(((datetime.timestamp(bot_message.created_at)-datetime.timestamp(message.created_at))%1)*1000)}ms " + str(message.author.mention))
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'say'):
                sent_message = message.content.replace(prefix + 'say ', "") #remove command and prefix at the beginning, leaving only the thing that you want the bot to say
                await message.channel.send(sent_message)
                await message.delete()
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'range'):
                range_string = message.content.replace(prefix + 'range ', "")
                range1 = range_string.partition(',')[0].replace(',', '')
                range2 = range_string.partition(',')[2].replace(',', '')
                print(range1, range2)
                try:
                	sent_message = str(random.randrange(int(range1), int(range2)))
                except ValueError as e:
                	sent_message = f"range accepts only numbers\nTraceback:{str(e)}"
                await message.channel.send(sent_message)
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'math'):
                math_string = message.content.replace(prefix + 'math ', "")
                if math_string.startswith('eval('):
                    await message.channel.send("lmao did you just try to execute an eval statement? bold of you to assume I am dumb enough to use an eval")
                else:
                    indiemath = list(math_string) 
                    whitespace = " "
                    while (whitespace in indiemath):
                        indiemath.remove(whitespace)
                    for math in indiemath:
                        if math == '+':
                            indiemath = list(math_string.split('+'))
                            sent_message = operator.add(int(indiemath[0]), int(indiemath[1]))
                            break
                        elif math == '-':
                            indiemath = list(math_string.split('-'))
                            sent_message = operator.sub(int(indiemath[0]), int(indiemath[1]))
                            break
                        elif math == '*':
                            indiemath = list(math_string.split('*'))
                            sent_message = operator.mul(int(indiemath[0]), int(indiemath[1]))
                            break
                        elif math == '/':
                            indiemath = list(math_string.split('/'))
                            sent_message = operator.truediv(int(indiemath[0]), int(indiemath[1]))
                            break
                        else:
                            sent_message = "not an operator, get punked"
                    await message.channel.send(sent_message)
                    log_message(message, sent_message)
            if message.content.startswith(prefix + 'eval'):
                if str(message.author.id) == "680959829426438168":
                	guild_name = discord.Guild.name
                	evalstate = message.content.replace(prefix + 'eval ', "")
                	sent_message = f'{eval(evalstate)}' #why does this not work?
                	await message.channel.send(sent_message)
                	log_message(message, sent_message)
                else:
                    guild_name = discord.Guild.name
                    sent_message = "haha you\'re not the owner of the bot so you cant use it"
                    await message.channel.send(sent_message)
                    log_message(message, sent_message)
            if message.content.startswith(prefix + 'owo '):
                index = random.randrange(0, len(owo))
                sent_message = owo[index]
                if message.content.replace(prefix + 'owo', "") != "":
                    sent_message = message.content.replace(prefix + 'owo', "") + " " + owo[index]
                await message.channel.send(sent_message)
                await message.delete()
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'translate-old '):
            #i really need a specified reference command lmao
                if message.content.replace(prefix + 'translate-old ', "").lower() == "helluva boss" or message.content.replace(prefix + 'translate-old ', "").lower() == "helluvaboss":
                    sent_message = "When I'm lonely, I become hungry...and when I become hungry, I want to choke on that red ████ of yours! ████ your █████ and lick all of your █████ before taking out your █████ and ████ with more teeth until you're screaming ████████ like a fucking baby!" #reference 3, and 3x2=6 and 6+6+6 = 666, show takes place in hell, this is epic
                    await message.channel.send(sent_message)
                    log_message(message, sent_message)
                    return
                count = 0
                await message.channel.send("WARNING: COMMAND LITERALLY DOESNT DO ANYTHING")
            if message.content.startswith(prefix + 'owoify '):
                sent_message = message.content.replace(prefix + 'owoify ', "")
                sent_message = sent_message.replace("r", "w")
                sent_message = sent_message.replace("u", "w")
                await message.channel.send(sent_message)
                await message.delete()
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'translate '):
                trans= Translator(to_lang="en", from_lang='autodetect')
                bot_message = await message.channel.send("Translating...")
                sent_message = trans.translate(message.content.replace(prefix + 'translate ', ''))
                sent_message = sent_message.replace("! / translate ", "")
                await bot_message.edit(content=sent_message)
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'credits'):
                sent_message = credits
                await message.channel.send(sent_message)
                log_message(message, sent_message)
            if message.content == prefix + 'help':
                sent_message = help_message
                await message.channel.send(sent_message)
                log_message(message, sent_message)
            if message.content == prefix + 'github':
                sent_message = 'Find our github at <https://github.com/Ruthenic/yadiscord-bot>!'
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
        try:
            botid = open (r'../botid.txt', "r")
            botid = botid.read() #read botID back into the var
        except:
            print("Please place valid bot ID in botid.txt beside main.py")
client = MyClient()
client.run(botid) #run with found botID

