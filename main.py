from nextcord.ext import commands
import os
from nextcord import Intents
bot = commands.Bot(command_prefix=['c!'], intents=Intents.all(), help_command=None)
@bot.command()
async def reload(ctx):
  for fn in os.listdir("./cogs"): 
    if fn.endswith('.py'): bot.reload_extension(f'cogs.{fn[: -3]}')
  await ctx.send('Reloaded mom')
for fn in os.listdir("./cogs"): 
  if fn.endswith('.py'): bot.load_extension(f'cogs.{fn[: -3]}')
bot.run(os.environ['token'])
