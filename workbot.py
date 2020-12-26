import time
import discord
import workToken
from datetime import datetime

TOKEN = workToken.tkn
t0 = None

client = discord.Client()

def twelveHrClock(hour):
    global currMeridiem
    currMeridiem = 'A.M.'
    d = {'13':'1', '14':'2', '15':'3', '16':'4', '17':'5',
         '18':'6', '19':'7', '20':'8', '21':'9', '22':'10',
         '23':'11', '24':'12'}
    if int(hour) > 12:
        hour = d[hour]
        currMeridiem = 'P.M.'
    return hour

@client.event
async def on_message(message):
    now = datetime.now()
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!start'):
        global t0
        t0 = time.time()
        hrStarted = twelveHrClock(now.strftime('%H'))
        minStarted = now.strftime('%M')
        day = now.strftime('%m/%d/%Y')
        await message.channel.send('Session started at {0}:{1} {2} on {3}'.format(hrStarted, minStarted, currMeridiem, day))

    if message.content.startswith('!finish'):
        hrEnded = twelveHrClock(now.strftime('%H'))
        minEnded = now.strftime('%M')
        day = now.strftime('%m/%d/%Y')
        t1 = time.time()
        total = t1-t0
        await message.channel.send('Session ended at {0}:{1} {2} on {3}'.format(hrEnded, minEnded, currMeridiem, day))
        await message.channel.send('Time taken: {0}'.format(total))
 
    
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)