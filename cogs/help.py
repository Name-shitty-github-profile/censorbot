from nextcord.ext import commands
from nextcord import Embed

class Help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def help(self, ctx):
    embed = Embed(title='Help', color = 0xe67e22).add_field(name='example', value='Test your settings').add_field(name='addword', value='Add a word to your bad word list')
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Help(bot))