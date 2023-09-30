#!/usr/bin/env python3

from disnake.ext import commands
import disnake
import config
import os
from evalogger import EvaLogger

intents = disnake.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True
intents.guilds = True
intents.members = True

client = disnake.Client(intents=intents)

bot = commands.InteractionBot(intents=intents)

log = EvaLogger(name="bot")
log.save_to_file = True
log.file_name = "bot.log"


for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')





# write general commands here

if __name__ == "__main__":
    bot.run(config.token)
