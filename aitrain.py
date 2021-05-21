from textgenrnn import textgenrnn
import discord
from discord.ext import commands
import regex as re

textgen = textgenrnn(name="insert3")
client = commands.Bot(command_prefix='.')
boton = 0

@client.event
async def on_message(message):
    await client.process_commands(message)
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',message.content.lower())
    if not message.attachments:
        if boton == 1:
            if message.content.lower().startswith("$"):
                pass
            elif urls:
                pass
            elif message.author.bot:
                pass
            elif message.content.lower().startswith("p!"):
                pass
            elif message.content.lower().startswith("—"):
                pass
            else:
                print(message.clean_content)
                train = open("train.txt", "a")
                train.write(f"{message.clean_content} \n")
                train.close()

@client.command()
async def train(ctx):
    if ctx.author.id == 666378959184855042:
        global boton
        boton = 1
        await ctx.send("I am now training what to say based on your messages")

@client.command()
async def stopbot(ctx):
    if ctx.author.id == 666378959184855042:
        await ctx.send("data collection done, I will now log of discord and build an a.i")
        textgen.train_from_file('train.txt', num_epochs=11)


client.run('BOTTOKEN')
