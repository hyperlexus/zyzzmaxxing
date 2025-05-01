import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils.data_manager import get_data, save_data

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='g.', intents=intents)

def load_cogs(bot):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    await bot.change_presence(activity=discord.Game(name='GET THE FUCK UP'))
    load_cogs(bot)
    await bot.sync_commands()

bot.data = get_data()
bot.save_data = lambda: save_data(bot.data)

bot.run(TOKEN)
