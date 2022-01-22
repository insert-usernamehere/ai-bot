from textgenrnn import textgenrnn
import discord
from discord.ext import commands
import regex as re
import functools
from aitextgen import aitextgen
import subprocess
from chatterbot import ChatBot

textgen = textgenrnn('insert3_weights.hdf5')
ai = aitextgen()
bot = ChatBot(
    'insert3',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)
client = commands.Bot(command_prefix='.')
boton = True

def add_to_train(clean_content):
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
            elif message.content.lower().startswith("."):
                pass
            elif message.content.lower().startswith("?"):
                pass
            elif message.content.lower().startswith("!"):
                pass
            elif message.content.lower().startswith("—"):
                pass
            elif message.content.lower().startswith("--"):
                pass
            else:
                writing_function = functools.partial(add_to_train, message.clean_content)
                await client.loop.run_in_executor(None, writing_function)
    if message.channel.id == 934533774249713664:
        if message.author.bot != True:
            bot_response = bot.get_response(message.clean_content)
            await message.channel.send(bot_response)

@client.command()
async def aiquote(ctx):
    try:
        textgen.generate_to_file('insert3.txt', n=1)
        with open("insert3.txt") as f:
            quote = f.read()
        await ctx.send(quote)
    except:
        textgen.generate_to_file('insert3.txt', n=1)
        with open("insert3.txt") as f:
            quote = f.read()
        await ctx.send(quote)

@client.command()
async def aiprompt(ctx):
    prompt = ctx.message.content[10:]
    endmsg = subprocess.check_output(['python3','promptai.py',f'{prompt}'])
    non = endmsg.replace("%1B[1m".encode(), "**".encode())
    nona = non.replace("%1B[0m".encode(), "**".encode())
    nor = nona.replace("[1m".encode(), "".encode())
    nora = nor.replace("[0m".encode(), "".encode())
    norx = nora.replace("\x1b[1m".encode(), "".encode())
    nore = norx.replace("\\x1b[1m".encode(), "".encode())
    nor1 = nore.replace("\x1b[0m".encode(), "".encode())
    nor2 = nor1.replace("\\x1b[0m".encode(), "".encode())
    finalmsg = nor2.decode("utf-8")
    print(finalmsg)
    await ctx.send(finalmsg)
    
    

@client.command()
async def aidel(ctx):
    await ctx.message.delete()
    try:
        textgen.generate_to_file('insert3.txt', n=1)
        with open("insert3.txt") as f:
            quote = f.read()
        await ctx.send(quote)
    except:
        textgen.generate_to_file('insert3.txt', n=1)
        with open("insert3.txt") as f:
            quote = f.read()
        await ctx.send(quote)


client.run('bot token')
