from nextcord.ext import commands
import os
from nextcord import Intents
bot = commands.Bot(command_prefix=['c!'], intents=Intents.all(), help_command=None)
@bot.command()
async def reload(ctx):
  for fn in os.listdir("./cogs"): bot.reload_extension(f'cogs.{fn[: -3]}') if fn.endswith('.py') else print('no code')
  await ctx.send('Reloaded mom')
for fn in os.listdir("./cogs"): bot.load_extension(f'cogs.{fn[: -3]}') if fn.endswith('.py') else print('no code')
bot.run(os.environ['token'])
