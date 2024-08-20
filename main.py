import discord
from discord.ext import tasks
from io import BytesIO
import random
import datetime as dt
import asyncio
import time
import os
from keep_alive import keep_alive
from PIL import Image, ImageDraw
import textblob
from textblob import TextBlob

watch_list = []

my_secret = os.environ['Maintok']
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Be a pookie please'))
    print("running")
    timecounting.start()  # Start the loop here
    keep_alive()

@client.event 
async def on_member_join(member):
     channel = client.get_channel(1205471447603089409)
     emb = discord.Embed(title="NEW MEMBER", description=f"Thanks {member.mention} for joining!")
     await channel.send(embed=emb)
     await channel.send(f"Welcome to the server {member.mention}! Tell us your age and tell us where ur from you ape.")

async def daily_job():
    print("Preparing...")
    server = client.get_guild(1205471447146045450)
    if not server:
        print("Server not found.")
        return

    dailyvictim = random.choice(server.members)

    while dailyvictim.bot:
        print("Bot detected, rerolling...")
        dailyvictim = random.choice(server.members)

    channel = client.get_channel(1205471447603089409)

    if not channel:
        print("Channel not found.")
        return

    shittalk = ["Speak fag!", "Speak ape", "Talk monki"]
    message = random.choice(shittalk)

    await sending(f"{message} {dailyvictim.mention}")
    print(f"{message} {dailyvictim.mention}")

@tasks.loop(seconds=60)
async def timecounting():
    current_time = dt.datetime.now().strftime("%H : %M")
    print(current_time)
    if current_time == "17 : 00":
        await daily_job()
        print(3)

async def sending(messagetosend):
    channel = client.get_channel(1205471447603089409)
    await channel.send(messagetosend)


@client.event
async def on_message(msg):
    newmessage = msg.content.lower()
    if msg.author == client.user:
        return
        
    if client.user.mentioned_in(msg):
        blob = TextBlob(msg.content)
        sentiment = blob.sentiment
        if sentiment <0.1 :
            await msg.reply("☹️")
        if sentiment > 0.1:
            await msg.reply("😊")
        else: 
            await msg.reply("?")
    
    Mentionedlen = len(msg.raw_mentions) + 1
    found = False
    if Mentionedlen > 20:
        for i in range(len(watch_list)):
            if str(msg.author.id) == str(watch_list[i]):
                found = True
                await msg.author.send("Too bad I warned you lool🤣🤣")
                await msg.delete()
                await asyncio.sleep(0.5)
               
                user = await client.fetch_user(934583471681187890)
                await user.send("Some bored bozo really tried raiding us " + str(msg.author.id))
                user2 = await client.fetch_user(624255198822662145)
                await user2.send("Some bored bozo really tried raiding us " + str(msg.author.id))
                watch_list.remove(watch_list[i])
                break
        if not found:
            await msg.author.send("This is a warning don't mention so many people at once bozo")
            watch_list.append(msg.author.id)
    else:
        for i in range(len(watch_list)):
            if str(msg.author.id) == str(watch_list[i]):
                watch_list.remove(watch_list[i])
                break
    

    if "!-!-!talkshit" in newmessage:
        if msg.author.id == 934583471681187890 or msg.author.id == 624255198822662145:
            await msg.delete()
            newermessage = newmessage.replace("!-!-!talkshit", "")
            await msg.channel.send(newermessage)

    if "!create!vc!" in newmessage:
        newermessage = newmessage.replace("!create!vc!", "")
        mainmessage = newermessage.replace(" ", "-")
        voice_state = msg.author.voice
        if voice_state is None:
            await msg.channel.send("Join vc pretty please")
        else:
            await msg.channel.send("Say less it will remove itself when there's no people in it")
            Category = client.get_channel(1274530224893329470)
            channel = await msg.guild.create_voice_channel(mainmessage, overwrites=None, category=Category, reason=None)
            await msg.author.move_to(channel)
    if "jfjdjjdjdjsnsjsnj6" in newmessage:
        print("DELETION STARTING!!!!!")
        channel = client.get_channel(730839966472601622)
        messages = await msg.channel.history(limit=500000).flatten()
        print(messages)
        for i in range(len(messages)):
            print("looking")
            if messages[i].author.id == 934583471681187890:
                await messages[i].delete()
                print("deleted")
                time.sleep(1)
    check = msg.content.split(" ")
    for i in range(len(check)):
                                if check[i].lower() == "faggot" or check [i].lower() == "cunt" or check[i].lower() == "retard":
                                    await msg.reply("spread the love 🥰")
                                    
                                if check[i].lower() == "!-!-!bully":
                                      if len(check) <2 or len(check) >5:
                                          await msg.channel.send("Don't try to be an idiot and break the bot, only leave one space in between the **SINGLE** tag and make sure there is only one argument, clean-ups in the future will happen.")
                                      else:
                                          person1a = ""
                                          guild = msg.guild
                                          for i in str(check[1]):
                                            if i.isdigit() == True:
                                                person1a = person1a + i 

                                          for member in guild.members:
                                              if member.id == int(person1a):
                                                person1 = member





                                          Marriage = Image.open("bullying.jpg")
                                          asset1 = person1.display_avatar.with_size(128)  # Updated line
                                          data1 = BytesIO(await asset1.read())  # Updated line
                                          pfp1 = Image.open(data1)
                                          pfp1 = pfp1.resize((140,140))
                                          bigsize = (pfp1.size[0] * 3, pfp1.size[1] * 3)
                                          mask = Image.new('L', bigsize, 0)
                                          draw = ImageDraw.Draw(mask) 
                                          draw.ellipse((0, 0) + bigsize, fill=255)
                                          mask = mask.resize(pfp1.size, )
                                          pfp1.putalpha(mask)

                                          Marriage.paste(pfp1,(584,190))
                                          Marriage.save("TEMP_HOLDER2.PNG")
                                          time.sleep(1)
                                          with open('TEMP_HOLDER2.PNG', 'rb') as f:
                                            picture = discord.File(f)
                                            await msg.channel.send(file=picture)
    

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is not None and after.channel is not before.channel:
        guild = client.get_guild(971601424595173376)
        for channel in guild.voice_channels:
            if channel.category_id == 975050220436070410:
                if len(channel.members) == 0:
                    await channel.delete()

client.run(my_secret)
