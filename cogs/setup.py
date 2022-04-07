from nextcord.ext import commands
import nextcord
from nextcord import Embed
from replit import db

class Setup(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def setup(self, ctx):
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in ctx.author.guild_permissions if p[1]])
    minperm = [
      'admin'
    ]
    if not any(word in perm_string.lower() for word in minperm): return await ctx.send('You cannot do this !')
    def check(reaction, user):
      return user.id == ctx.author.id and str(reaction.emoji) in ['✅', '❌']
    yes = '✅'
    no = '❌'
    embed = Embed(title='Do you want the word censor ?', description='Censor the word on your bad word list(addword to add a word removeword to remove a word and the list will have some few words at first)', color = 0xe67e22)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(yes)
    await msg.add_reaction(no)
    reaction, user = await self.bot.wait_for('reaction_add', check=check)
    if str(reaction.emoji) == yes:
      db[f'msgcensor{ctx.guild.id}'] = True
    elif str(reaction.emoji) == no:
      db[f'msgcensor{ctx.guild.id}'] = False
    embed = Embed(title="What do you want the message that the bot will send to the user in the chat to be?", description='Look at the image for an example', color = 0xe67e22).set_image(url='https://cdn.discordapp.com/attachments/939311233272799282/961372301167824916/2022-04-06_17-10-02.gif')
    await ctx.send(embed=embed)
    def checkmsg(m):
      return m.author.id == ctx.author.id and ctx.channel.id == m.channel.id
    msg = await self.bot.wait_for('message', check=checkmsg)
    db[f'badmsg{ctx.guild.id}'] = msg.content
    embed = Embed(title="What do you want the message that the bot will send to the user in their dms to be?", description='Send a message in their dms', color = 0xe67e22)
    await ctx.send(embed=embed)
    msg = await self.bot.wait_for('message', check=checkmsg)
    db[f'badmsgdm{ctx.guild.id}'] = msg.content
    embed = Embed(title="What is the log channel id ?", description='Send a sort of logs', color = 0xe67e22).set_image(url='https://cdn.discordapp.com/attachments/939311206089523211/961620636759887932/2022-04-06_17-30-09.gif')
    await ctx.send(embed=embed)
    msg = await self.bot.wait_for('message', check=checkmsg)
    db[f'logchan{ctx.guild.id}'] = int(msg.content)
    embed = Embed(title='Do you want the username censor ?', description='Censor the word on the username on your bad word list(addword to add a word removeword to remove a word and the list will have some few words at first)', color = 0xe67e22)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(yes)
    await msg.add_reaction(no)
    reaction, user = await self.bot.wait_for('reaction_add', check=check)
    if str(reaction.emoji) == yes:
      db[f'namecensor{ctx.guild.id}'] = True
    elif str(reaction.emoji) == no:
      db[f'namecensor{ctx.guild.id}'] = False
    embed = Embed(title='You have finished !', description='This bot can have some updates so please redo the setup every month', color = 0xe67e22)
    await ctx.send(embed=embed)
    
    
    


def setup(bot):
  bot.add_cog(Setup(bot))