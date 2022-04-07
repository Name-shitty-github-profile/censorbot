from nextcord.ext import commands
from nextcord import Embed
from replit import db
class wordcensorcogs(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_message')
  async def wordcensor(self, message):
    if message.author.bot: return
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in message.author.guild_permissions if p[1]])
    minperm = [
      'admin'
    ]
    if not any(word in perm_string.lower() for word in minperm): return
    if not message.guild:
      return
    else:
      if f'msgcensor{message.guild.id}' not in db.prefix('msgcensor'):
        censorwordsys = False
      else:
        censorwordsys = db[f'msgcensor{message.guild.id}']
      if censorwordsys:
        if f'badwordlist{message.guild.id}' not in db.prefix('badwordlist'):
          badlist = [
            'fag',
            'nig',
            'tranny'
          ]
        else:
          badlist = db[f'badwordlist{message.guild.id}']
        if any(word in message.content.lower() for word in badlist):
          await message.delete()
          if f'badmsg{message.guild.id}' not in db.prefix('badmsg'):
            badmsg = 'You cannot say this word !'
          else:
            badmsg = db[f'badmsg{message.guild.id}']
          await message.channel.send(badmsg)
          if f'badmsgdm{message.guild.id}' not in db.prefix('badmsgdm'):
            badmsgdm = f"You can't say this in this server ({message.guild.name})\nMessage content : ||{message.content}||"
          else:
            badmsgdm = f"{str(db[f'badmsg{message.guild.id}'])}\nMessage content : ||{message.content}||"
          await message.author.send(badmsgdm)
          if f'logchan{message.guild.id}' in db.prefix('logchan'):
            logchannelid = db[f'logchan{message.guild.id}']
            logchan = message.guild.get_channel(logchannelid)
            embed = Embed(title=f'{message.author.name} bad word', description=f'**message content**\n||{message.content}||', color = 0xe67e22).add_field(name='Message sent', value=badmsgdm).add_field(name='Message sent in the chat', value=badmsg)
            await logchan.send(embed=embed)
          
      else:
        return

  @commands.Cog.listener('on_message_edit')
  async def wordcensoredit(self, before, message):
    if message.author.bot: return
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in message.author.guild_permissions if p[1]])
    minperm = [
      'admin'
    ]
    if not any(word in perm_string.lower() for word in minperm): return
    if not message.guild:
      return
    else:
      if f'msgcensor{message.guild.id}' not in db.prefix('msgcensor'):
        censorwordsys = False
      else:
        censorwordsys = db[f'msgcensor{message.guild.id}']
      if censorwordsys:
        if f'badwordlist{message.guild.id}' not in db.prefix('badwordlist'):
          badlist = [
            'fag',
            'nig',
            'tranny'
          ]
        else:
          badlist = db[f'badwordlist{message.guild.id}']
        if any(word for word in message.content.lower() in badlist):
          await message.delete()
          if f'badmsg{message.guild.id}' not in db.prefix('badmsg'):
            badmsg = 'You cannot say this word !'
          else:
            badmsg = db[f'badmsg{message.guild.id}']
          await message.channel.send(badmsg)
          if f'badmsgdm{message.guild.id}' not in db.prefix('badmsgdm'):
            badmsgdm = f"You can't say this in this server ({message.guild.name})\nMessage content : ||{message.content}||"
          else:
            badmsgdm = f"{str(db[f'badmsg{message.guild.id}'])}\nMessage content : ||{message.content}||"
          await message.author.send(badmsgdm)
          if f'logchan{message.guild.id}' in db.prefix('logchan'):
            logchannelid = db[f'logchan{message.guild.id}']
            logchan = message.guild.get_channel(logchannelid)
            embed = Embed(title=f'{message.author.name} bad word', description=f'**message content**\n||{message.content}||', color = 0xe67e22).add_field(name='Message sent', value=badmsgdm).add_field(name='Message sent in the chat', value=badmsg)
            await logchan.send(embed=embed)
          
      else:
        return
        
def setup(bot):
  bot.add_cog(wordcensorcogs(bot))