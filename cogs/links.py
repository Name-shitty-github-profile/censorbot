from nextcord.ext import commands
from nextcord import Embed

class Links(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def links(self, ctx):
    embed = Embed(title='Links', description=f'\n\nClick [here](https://discord.com/api/oauth2/authorize?client_id=956682155466051614&permissions=8&scope=bot%20applications.commands) do add me\n\nClick [here](https://discord.gg/bNUNcnjK3r) to join the suppport server', color = 0xe67e22)
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Links(bot))