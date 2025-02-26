import discord; from discord.ext import commands
import asyncio
import config
from core.bot import Bot

bot = Bot()

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")
    

@bot.event
async def on_connect():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="-help | @Moon Beatz"))
    
    
async def main():
    async with bot:
        await bot.start(config.TOKEN)
        
if __name__ == "__main__":
    asyncio.run(main())