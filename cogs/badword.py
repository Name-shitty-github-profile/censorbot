from nextcord.ext import commands
from nextcord import Embed
from replit import db
class Badword(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def addword(self, ctx, word = None):
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in ctx.author.guild_permissions if p[1]])
    minperm = [
      'admin'
    ]
    if not any(word in perm_string.lower() for word in minperm): return await ctx.send('You cannot do this !')
    def check(m):
      return m.author.id == ctx.author.id and ctx.channel.id == m.channel.id
    if not word:
      await ctx.send('Wich word do you want to add to the list ?')
      msg = await self.bot.wait_for('message', check=check)
    word = msg.content
    if f'badwordlist{ctx.guild.id}' not in db.prefix('badwordlist'):
      badlist = [
        'fag',
        'nig',
        'tranny'
      ]
    else:
      badlist = db[f'badwordlist{ctx.guild.id}']
    if word in badlist: return await ctx.send('This word is already in the list')
    badlist.insert(word.lower())
    db[f'badwordlist{ctx.guild.id}'] = badlist
    embed = Embed(title='New word added to the censored word list !', description='The word is treated with no caps so you cannot wrote it', color = 0x1f8b4c)
    await ctx.send(embed=embed)

  @commands.command()
  async def removeword(self, ctx, word = None):
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in ctx.author.guild_permissions if p[1]])
    minperm = [
      'admin'
    ]
    if not any(word in perm_string.lower() for word in minperm): return await ctx.send('You cannot do this !')
    def check(m):
      return m.author.id == ctx.author.id and ctx.channel.id == m.channel.id
    if not word:
      await ctx.send('Wich word do you want to remove from the list ?')
      msg = await self.bot.wait_for('message', check=check)
    word = msg.content
    if f'badwordlist{ctx.guild.id}' not in db.prefix('badwordlist'):
      badlist = [
        'fag',
        'nig',
        'tranny'
      ]
    else:
      badlist = db[f'badwordlist{ctx.guild.id}']
    if word not in badlist: return await ctx.send('This word is not in the list')
    badlist.remove(word.lower())
    db[f'badwordlist{ctx.guild.id}'] = badlist
    embed = Embed(title=f'{word} removed from the censored word list !', description='The word is treated with no caps so you cannot wrote it', color = 0x1f8b4c)
    await ctx.send(embed=embed)

  @commands.command()
  async def badword(self, ctx):
    alllist = ''
    if f'badwordlist{ctx.guild.id}' not in db.prefix('badwordlist'):
      badlist = [
        'fag',
        'nig',
        'tranny'
      ]
    else:
      badlist = db[f'badwordlist{ctx.guild.id}']
    for word in badlist:
      alllist = f'{alllist}\n`{word}`'
    embed = Embed(title='Bad word list', description=alllist, color = 0x1f8b4c)
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Badword(bot))