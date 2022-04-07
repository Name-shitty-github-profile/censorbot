from nextcord.ext import commands
from nextcord import Embed
from replit import db
class Example(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def example(self, ctx):
    await ctx.message.delete()
    if f'badmsg{ctx.message.guild.id}' not in db.prefix('badmsg'):
      badmsg = 'You cannot say this word !'
    else:
      badmsg = db[f'badmsg{ctx.message.guild.id}']
    await ctx.send(badmsg)
    if f'badmsgdm{ctx.message.guild.id}' not in db.prefix('badmsgdm'):
      badmsgdm = f"You can't say this in this server ({ctx.message.guild.name})\nMessage content : ||{ctx.message.content}||"
    else:
      badmsgdm = f"{str(db[f'badmsg{ctx.message.guild.id}'])}\nMessage content : ||{ctx.message.content}||"
    await ctx.author.send(badmsgdm)
    embed = Embed(title=f'{ctx.message.author.name} bad word', description=f'**message content**\n||{ctx.message.content}||', color = 0xe67e22).add_field(name='Message sent', value=badmsgdm).add_field(name='Message sent in the chat', value=badmsg)
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Example(bot))