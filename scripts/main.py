import discord
from discord import File
import random
import traceback
import os
import subprocess
import operator
import array as arr
import time
from datetime import datetime
from google_trans_new import google_translator 
import json
from rapidapis import *
from PyDictionary import PyDictionary
try:
    import tesm.main as tesm
except:
    import tesm as tesm
import requests
    
dictionary=PyDictionary()
credits = " People who've contributed: \nRuthenic (AD/Drake),\ntestersbastarps (onboho),\nGnog3 (Gnog3)"
help_message = 'YaDiscord Bot\'s commands:\n`!/help` Show the command list.\n`!/credits` Basically credits.\n`!/ping` Ping the bot.\n`!/owo` Print a random OwO/UwU\n`!/say (text)` Make the bot say something.\n`!/range (first-number), (second-number)` Make the bot generate a random number in given range.\n`!/math (math-stuff)` Do simple math\n`!/eval` Evaluate something. Owner only.' #very long string, i know. do i care? no
prefix = '!/'
owo = ['owo', 'OwO', 'oWo', 'OWO', 'uwu', 'UwU', 'uWu', 'UWU'] #owo
limit = 2000
intents = discord.Intents(members=True)
intents.members = True
client = discord.Client(intents=intents)

def log_message(user_message, sent_message): #log commands and their replies
    #reference go brrrr
    print(f'\nMessage hazbin sent in response to \'{user_message.content}\'\nResponse: {sent_message}\nUser: {user_message.author}, UserID: {user_message.author.id}\nGuild: {user_message.guild.name}, GuildID: {user_message.guild.id}\nChannel: {user_message.channel.name}, ChannelID:{user_message.channel.id}') # onboho says hi again :)  
        
class MyClient(discord.Client):
    async def on_ready(self): 
        print('Logged in as', self.user)
    async def on_message(self, message):
        if str(message.author.id) == '795683912990851072' or str(message.author.id) == '796227553911242762':
            return #dont reply to the bot itself
        try:
            if message.content == prefix + 'ping':
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
                sent_message = str(random.randrange(int(range1), int(range2)))
                await message.channel.send(sent_message)
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'math'):
                math_string = message.content.replace(prefix + 'math ', "")
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
                        sent_message = "not an operator and/or not a simple math statement, get punked"
                await message.channel.send(sent_message)
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'eval'):
                if str(message.author.id) == "714583473804935238":
                	evalstate = message.content.replace(prefix + 'eval ', "")
                	sent_message = str(eval(evalstate))
                	#for stdline in sent_message:
                	#    new_sent_message = new_sent_message + stdline + "\n"
                	#sent_message = new_sent_message
                	await message.channel.send(sent_message)
                	log_message(message, sent_message)
                else:
                    guild_name = discord.Guild.name
                    sent_message = "haha you\'re not the owner of the bot so you can't use it"
                    await message.channel.send(sent_message)
                    log_message(message, sent_message)
            if message.content.startswith(prefix + 'owo'):
                sent_message = owo[random.randrange(0, len(owo))]
                if not message.content.replace(prefix + 'owo', "") == "":
                    sent_message = message.content.replace(prefix + 'owo', "") + " " + owo[random.randrange(0, len(owo))]
                await message.channel.send(sent_message)
                await message.delete()
                log_message(message, sent_message)
            '''if message.content.startswith(prefix + 'translate-old '):
            #i really need a specified reference command lmao
                if message.content.replace(prefix + 'translate-old ', "").lower() == "helluva boss" or message.content.replace(prefix + 'translate-old ', "").lower() == "helluvaboss" or message.content.replace(prefix + 'translate-old ', "").lower() == "helluva":
                    sent_message = "When I'm lonely, I become hungry...and when I become hungry, I want to choke on that red ████ of yours! ████ your █████ and lick all of your █████ before taking out your █████ and ████ with more teeth until you're screaming ████████ like a fucking baby!" #reference 3, and 3x2=6 and 6+6+6 = 666, show takes place in hell, this is epic
                    await message.channel.send(sent_message)
                    log_message(message, sent_message)
                    await message.delete()
                    return
                if message.content.replace(prefix + 'translate-old ', "").lower() == "hazbin hotel" or message.content.replace(prefix + 'translate-old ', "").lower() == "hazbinhotel" or message.content.replace(prefix + 'translate-old ', "").lower() == "hazbin":
                    sent_message = "Oh, harder daddy!" #reference 4 because 4 is cool
                    await message.channel.send(sent_message)
                    log_message(message, sent_message)
                    await message.delete()
                    return
                count = 0
                await message.channel.send("WARNING: COMMAND LITERALLY DOES NOT DO ANYTHING")''' #imagine having an old command
            if message.content.startswith(prefix + 'owoify '):
                sent_message = message.content.replace(prefix + 'owoify ', "").replace("r", "w").replace("u", "w")
                await message.channel.send(sent_message)
                await message.delete()
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'translate '):
                trans = google_translator()
                bot_message = await message.channel.send("Translating...")
                sent_message = trans.translate(message.content.replace(prefix + 'translate ', ''), lang_tgt = 'en')
                await bot_message.edit(content=sent_message)
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'Übersetzen ') or message.content.startswith(prefix + 'translate-de '):
                trans = google_translator()
                bot_message = await message.channel.send("Übersetzen...")
                sent_message = trans.translate(message.content.replace(prefix + 'translate-de ', ''), lang_tgt = 'de')
                await bot_message.edit(content=sent_message)
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'translate-ru '):
                trans = google_translator()
                bot_message = await message.channel.send("Translating...")
                sent_message = trans.translate(message.content.replace(prefix + 'translate-ru ', ''), lang_tgt = 'ru')
                await bot_message.edit(content=sent_message)
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'urban') and message.content != prefix + "urbanrand":
                word = message.content.replace(prefix + 'urban ', "").replace(" ", "%20")
                try:
                    num = int(word[word.rfind("%20") + len("%20")])
                except Exception as e:
                    word = word + "%200"
                    num = int(word[word.rfind("%20") + len("%20")])
                word = "%20".join(word.split("%20")[:-1])
                result = urbdic.urban(word, num)
                sent_message = result["definition"].replace("[", "").replace("]", "") + "\n"
                examples = result["example"].split("\n")
                for example in examples:
                    example = "*" + example.strip().replace("[", "").replace("]", "")
                    sent_message = sent_message + example + "*\n"
                if len(sent_message) > limit:
                    tmp = []
                    for split in [sent_message[i:i+limit] for i in range(0, len(sent_message), limit)]:
                        tmp.append(split)
                    sent_message = []
                    for i in tmp:
                        sent_message.append(i)
                    for i in sent_message:
                        await message.channel.send(i)
                else:
                    await message.channel.send(sent_message)
                log_message(message, sent_message)
            if message.content == prefix + "urbrand":
                result = urbdic.urbrand()
                sent_message = result["Word"] + ":\n" + result["definition"].replace("[", "").replace("]", "") + "\n"
                examples = result["example"].split("\n")
                for example in examples:
                    example = "*" + example.strip().replace("[", "").replace("]", "")
                    sent_message = sent_message + example + "*\n"
                await message.channel.send(sent_message)
                log_message(message, sent_message)
            if message.content.startswith(prefix + "r34"):
                if message.channel.is_nsfw():
                    command = message.content.split(" ")
                    #tags = message.content.replace(prefix + "r34", "").lstrip(" ").split(",")
                    try:
                        tags = command[1].split(",")
                    except:
                        tags = []
                    if len(tags) == 0:
                        response = requests.get('https://r34-json.herokuapp.com/posts').text
                    else:
                        link = 'https://r34-json.herokuapp.com/posts?tags='
                        for i in tags:
                            link+=i + "+"
                        link = link.rstrip("+")
                        print(link)
                        response = requests.get(link).text
                    posts = json.loads(response)
                    if len(command) < 3:
                        post = posts["posts"][0]
                    else:
                        post = posts["posts"][int(command[2])]
                    link = post["file_url"]
                    title = post["id"]
                    score = post["score"]
                    embed=discord.Embed(title=title, description=score, url="https://rule34.xxx/index.php?page=post&s=view&id=" + post["id"])
                    embed.set_image(url=link)
                    #embed.add_field(name=undefined, value=undefined, inline=False)
                    await message.channel.send(embed=embed)
                    #print(post)
                    log_message(message, "[embed]")
                else:
                    await message.channel.send("Cannot display porn in non-nsfw channels")
            if message.content.startswith(prefix + "covidcountry "):
                result = covid19.covidcountry(message.content.replace(prefix + 'covidcountry ', ""))
                sent_message = "Confirmed cases in " + result['country'] + ": " + str(result['confirmed'])
                await message.channel.send(sent_message)
                log_message(message, sent_message)
            if message.content.startswith(prefix + "define"):
                sent_message = 'Finding definition...'
                bot_message = await message.channel.send(sent_message)
                result = dictionary.meaning(message.content.replace(prefix + "define", ""))
                new_message = []
                for i in result:
                    new_message.append("{}: {}".format(i,result[i][0]))
                sent_message = ''
                for i in new_message:
                    sent_message += i + '\n'
                await bot_message.edit(content=sent_message)
                log_message(message, sent_message)
            if message.content == prefix + "sc":
                n=0
                for i in client.guilds:
                    print(i)
                    n+=1
                await message.channel.send('Bot is in `{}` servers'.format(str(n)))
            if message.content.startswith(prefix + "angeldust"):
            	#secret command, tell no-one
            	await message.channel.send("gg\nhttps://youtu.be/gS5CHjROVH4")
            if message.content.startswith(prefix + 'credits'):
                sent_message = credits
                await message.channel.send(sent_message)
                log_message(message, sent_message)
            if message.content == prefix + 'help':
                try:
                    help_message = open (r'help.txt', "r")
                    sent_message = help_message.read()
                except:
                    try:
                        help_message = open (r'../help.txt', "r")
                        sent_message = help_message.read()
                    except:
                        await message.channel.send("Help file not found, defaulting to old string-based one. Sorry m8, can't help ya :(")
                        print("Error: cannot find help file, fallback to string")
                        sent_message = help_message
                await message.channel.send(sent_message)
                log_message(message, sent_message)
            if message.content == prefix + 'github':
                sent_message = 'Find our github at <https://github.com/Ruthenic/yadiscord-bot>!'
                await message.channel.send(sent_message)
                log_message(message, sent_message)
            if message.content.startswith(prefix + 'tesm'):
                code = message.content.split('```')[1].split('```')[0]
                ary = code.split('\n')
                code = []
                for i in ary:
                    code.append(i.split(' '))
                sent_message = tesm.interpret(code)
                await message.channel.send(sent_message)
                log_message(message, sent_message)
            if 'hell ' in message.content.lower():
                sent_message = "Stolas: Then let me keep it simple: once a month, on the full moon, you return the book to me, followed by a night of…\n*[Stolas’ eyes glow red and he lowers himself into the water with a lustful look]*\nStolas: ***…Passionate fornication.***\n*[...]*\nStolas: Oh, Blitzy! I’m so excited! I cannot wait to feel your slimy c**[bleep]**ck inside of my **[bleep]**. To **[bleep]** the— " #reference 3, and 3x2=6 and 6+6+6 = 666, show takes place in hell, this is epic
                await message.channel.send(sent_message)
                #log_message(message, sent_message)
            if 'hazbin' in message.content.lower():
                sent_message = "Oh, harder daddy!" #reference 4 because 4 is cool
                await message.channel.send(sent_message)
                #log_message(message, sent_message)
            if 'amogus' in message.content.lower() or 'amongus' in message.content.lower():
                sent_message = 'I don\'t even have a witty message for this please just stop saying it'
                await message.channel.send(sent_message)
            if message.content.startswith(prefix + 'stock'):
                info = stock.info(message.content.replace(prefix+'stock ', '').replace('$', ''))
            if message.content.startswith(prefix + 'request'): #pop on into checking for request things
                args = message.content.replace('!/', '').split(' ')
                if args[1] == 'help':
                    try:
                        help_message = open (r'help-request.txt', "r")
                        sent_message = help_message.read()
                    except:
                        try:
                            help_message = open (r'../help-request.txt', "r")
                            sent_message = help_message.read()
                        except:
                            await message.channel.send("Help file not found, defaulting to old string-based one. Sorry m8, can't help ya :(")
                            print("Error: cannot find help file, fallback to string")
                            sent_message = 'error'
                    await message.channel.send(sent_message)
                    log_message(message, sent_message)
                if args[1] == 'prompt':
                    user = client.get_channel(810668024105009185)
                    await user.send('{}, {} wants {} on {}, {}, with prompt "{}", on channel {}'.format(message.author.mention, message.author.id, args[1], message.guild.name, message.guild.id, message.content.replace('!/request prompt ', ''), message.channel.id))
                    await message.channel.send("Request sent!")
                if args[1] == 'voice':
                    user = client.get_channel(810668024105009185)
                    await user.send('{}, {} wants {} on {}, {}, with script "{}" and character {}, on channel {}'.format(message.author.mention, message.author.id, args[1], message.guild.name, message.guild.id, message.content.replace('!/request voice {} '.format(args[3]), ''), args[3], message.channel.id))                    
                    await message.channel.send("Request sent!")
                if args[1] == 'fulfill':
                    channel = client.get_channel(int(args[2]))
                    attachments = message.attachments
                    if attachments == []:
                        await channel.send(message.content.replace('!/request fulfill {} {} '.format(args[2], args[3]), ''))
                    else:
                        await attachments[0].save('request.{}'.format(attachments[0].filename.split('.')[1]))
                        await channel.send('request', file=File('request.{}'.format(attachments[0].filename.split('.')[1])))
                    await channel.send('Request fulfilled, <@!{}>!'.format(args[3]))
        except Exception as e:
            await message.channel.send(f"lol an error happened get cucked by the python code loser\nTraceback: {str(e)}") #lol
            traceback.print_exc()

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

