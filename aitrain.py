from textgenrnn import textgenrnn
import discord
from discord.ext import commands
import regex as re
import functools

textgen = textgenrnn(name="insert3")
client = commands.Bot(command_prefix='.')
boton = False

def add_to_train(clean_content):
    print(clean_content)
    with open("train.txt", "a") as train:
        train.write(f"{clean_content} \n")

@client.event
async def on_message(message):
    await client.process_commands(message)
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',message.content.lower())
    if not message.attachments:
        if boton:
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
                async with message.channel.typing:
                    writing_function = functools.partial(add_to_train, message.clean_content)
                    await bot.loop.run_in_executor(None, writing_function)

@commands.is_owner()
@client.command()
async def train(ctx):
    global boton
    boton = True
    await ctx.send("I am now training what to say based on your messages")

@commands.is_owner()
@client.command()
async def stopbot(ctx):
    async with ctx.typing:
        training_function = functools.partial(textgen.train_from_file, 'train.txt', num_epochs=11)
        await bot.loop.run_in_executor(None, training_function)
    await ctx.send("data collection done, I will now log of discord and build an a.i")
    await bot.logout()


client.run('BOTTOKEN')
