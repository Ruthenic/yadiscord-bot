import discord

class MyClient(discord.Client):
    async def on_ready(self): 
        print('Logged on as', self.user)
    async def message (stroing):
        if (stroing.startsWith('!channelid.set')):
            
        await message.channel.send

print("Running on local machine. Using text file...") #if config var not found, utilize botid.txt for bot id
try:
    botid = open (r'botid.txt', "r")
    botid = botid.read() #read botID back into the var
except:
    print("Please place valid bot ID in botid.txt beside main.py")
client = MyClient()
client.run(botid) #run with found botID
while(True):
    
