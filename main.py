import discord
import random
import traceback
import os
import operator
import array as arr

letters = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
prefix = '!/'
def log_message(command, sent_message): #log commands and their replies
    #reference go brrrr
    print('Message hazbin sent in response to \'' + command + '\': ' + sent_message)#todo add user name, guild name, and channel name to log
class MyClient(discord.Client):
    async def on_ready(self): 
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return #dont reply to ourselves
        try:
            if message.content == prefix + 'ping':
                guild_name = discord.Guild.name
                sent_message = 'Pong!' #todo: put latency here
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
            if message.content.startswith(prefix + 'math'):
                math_string = message.content.replace(prefix + 'math ', "")
                if any(ext in math_string for ext in letters):
                    await message.channel.send("lmao did you just try to execute something with a letter in an eval statement? nonono, you cannnot do that")
                else:
                    #sent_message = str(eval(math_string))
                    sent_message = "Removed math function due to ability to crash python, and therefore the bot, with a large enough exponential equasion. Sorry for the inconvience - Man Behind the Machine"
                    await message.channel.send(sent_message)
                    log_message(message.content, sent_message)
                
                
        except Exception as e:
            await message.channel.send("lol an error happened get cucked by the python code loser\nTraceback: " + str(e)) #lol
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
