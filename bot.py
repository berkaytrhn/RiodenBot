import discord
from discord.ext import commands
import os 


#open("./token.txt").read()
botToken = os.environ["API-KEY"]

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

bot = commands.Bot(command_prefix=".", intents = intents)
client = discord.Client()

""" 
channel = discord.Object(id='827288797737123912')
"""


@bot.event
async def on_ready():
    print("Bot is ready")


''' @bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith(".hello"):
        await message.channel.send("Hello :)")
 '''

@bot.event
async def on_member_join(member):
    print("someone appeared in server {}".format(member))



@bot.event
async def on_member_remove(member):
    print("someone left server :( {}".format(member))


@bot.command()
async def ping(context):
    await context.send("Pong!! :) {}ms".format(round(bot.latency*1000)))

@bot.command(aliases=["play"])
async def game(context,*, text="None"):

    print(text)

    """ if len(arguments)>0:
        element = arguments[0]
        #print(arguments)
        print(text)
        await context.send(f"Hello bud, this is a basic game :))😀 {element}")
    else:
        await context.send(f"Hello bud, this is a basic game :))😀")
        #random.choice(list)  """




bot.run(botToken)
