import discord
client = discord.client
@client.event
async def on_ready():
  message.channel.send("Hello!")
