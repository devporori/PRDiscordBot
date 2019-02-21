import discord

client = discord.Client()

@client.event
async def on_ready():
    print("로그인")
    print(client.user.name)
    print(client.user.id)
    print("------------------")

@client.event
async def on_message(message):
    if message.content.startswith("pr!help"):
        await client.send_message(message.channel, "Test")

client.run('')