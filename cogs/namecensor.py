from nextcord.ext import commands, tasks
from nextcord import Embed
from replit import db
class namecensorcogs(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_member_update')
  async def namecensor(self, before, after):
    if f'namecensor{before.guild.id}' not in db.prefix('namecensor'): return
    if not db[f'namecensor{before.guild.id}']: return
    if f'badwordlist{after.guild.id}' not in db.prefix('badwordlist'):
      badlist = [
        'fag',
        'nig',
        'tranny'
      ]
    else:
      badlist = db[f'badwordlist{after.guild.id}']
    if any(word in after.name.lower() for word in badlist):
      await after.send(f'You need to change your name or you will be kicked from {after.guild.name}\n||You have 10 minutes||')
      if f'logchan{after.guild.id}' in db.prefix('logchan'):
        logchannelid = db[f'logchan{after.guild.id}']
        logchan = after.guild.get_channel(logchannelid)
        embed = Embed(title=f'{after.name} bad usernickname', description=f'**name**\n||{after.name}||\n\n**old name**\n{before.name}', color = 0xe67e22)
        await logchan.send(embed=embed)
        memberaftername = self.bot.get_user(int(after.id))
        if memberaftername.name == after.name:
          await after.send(f'You have been kicked from {after.guild.name}')
          await after.guild.kick(after)
        else:
          await after.send('Thanks for your change !')

  @tasks.loop(minutes=10.0)
  async def batch_update(self):
      for guild in self.bot.guilds:
        if f'namecensor{guild.id}' in db.prefix('namecensor'):
          if db[f'namecensor{guild.id}']:
            if f'badwordlist{guild.id}' not in db.prefix('badwordlist'):
              badlist = [
              'fag',
              'nig',
              'tranny'
              ]
            else:
              badlist = db[f'badwordlist{guild.id}']
            for member in guild.members:
              if any(word in member.name for word in badlist):
                await member.send(f'You need to change your name or you will be kicked from {guild.name}\n||You have 3 minutes||')
                if f'logchan{guild.id}' in db.prefix('logchan'):
                  logchannelid = db[f'logchan{guild.id}']
                  logchan = guild.get_channel(logchannelid)
                  embed = Embed(title=f'{member.name} bad usernickname', description=f'**name**\n||{member.name}||\n\n**old name**\n{member.name}', color = 0xe67e22)
                  await logchan.send(embed=embed)
                  memberaftername = self.bot.get_user(int(member.id))
                  if memberaftername.name == member.name:
                    await member.send(f'You have been kicked from {guild.name}')
                    await guild.kick(member)
                  else:
                    await member.send('Thanks for your change !')
          

        
def setup(bot):
  bot.add_cog(namecensorcogs(bot))