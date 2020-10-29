import discord

class MyClient(discord.Client):
    async def on_ready(self): 
        print('Logged on as', self.user)
    async def message(stroing):
        if (stroing.startsWith('!channelid.set')):
            message.channel = client.get_channel(int(stroing.replace('!channelid.set ', '')))
            print('Channel ID is now ' + stroing.replace('!channelid.set ', ''))
        else: 
            await message.channel.send(stroing)

print("Running on local machine. Using text file...") #if config var not found, utilize botid.txt for bot id
try:
    botid = open (r'botid.txt', "r")
    botid = botid.read() #read botID back into the var
except:
    print("Please place valid bot ID in botid.txt beside main.py")
client = MyClient()
client.run(botid) #run with found botID
while(True):
    a = input("Console> ")
    await MyClient.message(a)
