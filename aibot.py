from textgenrnn import textgenrnn
import discord
from discord.ext import commands
import regex as re

textgen = textgenrnn('insert3_weights.hdf5')
client = commands.Bot(command_prefix='.')


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


client.run('Nzk0MzgwMDQ5MzUxOTY2NzQy.X-5-Eg.5mYRMnHxHYqFQZKbbnY8cyTxOzQ')