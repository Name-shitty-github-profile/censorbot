from nextcord.ext import commands, tasks
import random
from nextcord import Game
class status(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_ready')
  async def printin(self):
    print('online !')

  @tasks.loop(minutes=3.0)
  async def status_update(self):
    activitylist = [
      'Being racist is bad',
      'Hi I am new here',
      'Hi',
      'Have a good day',
      'I hope everyone is doing great today',
      'Hi everyone'
    ]
    await self.bot.change_presence(activity=Game(name=str(random.choice(activitylist))))
          

        
def setup(bot):
  bot.add_cog(status(bot))