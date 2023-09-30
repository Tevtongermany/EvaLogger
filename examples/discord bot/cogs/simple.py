from disnake.ext import commands
import disnake
from evalogger import EvaLogger

class Simple(commands.Cog):
    """The description for Simple goes here."""
    def __init__(self, bot):
        self.bot = bot
        self.log = EvaLogger(name="bot")

    @commands.slash_command(name="log", description="log a message with evalogger")
    async def log(self,message:str,inter: disnake.CommandInteraction):
        self.log.info(message)
        await inter.send(message)

def setup(bot):
    bot.add_cog(Simple(bot))

