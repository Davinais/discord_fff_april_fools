from discord.ext import commands
import discord
import configparser

config = configparser.ConfigParser()
config.read('gochiusa.ini')

bot_ids = config['bot_ids']
channel_ids = config['channel_ids']
event_role_id = int(config['role_ids']['event_role'])
correct_channel = config['bot_correct_channel']

client = commands.Bot(command_prefix='!')

@client.command()
async def maydaymaydaymayday(ctx):
    await ctx.send("我孫女她們好像找不到自己回家的路了，你能使用你的「移動成員」能力把她們送回家嗎？")
    await ctx.send("輸入 `!check` 來讓我確定她們是不是真的都安全回家了吧")

@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

@client.command()
async def check(ctx):
    gochiusa_bots = { 
        name :
        discord.utils.get(ctx.message.guild.members, id=int(id)) for name, id in bot_ids.items()
    }
    channels = {
        name :
        discord.utils.get(ctx.message.guild.channels, id=int(id)) for name, id in channel_ids.items()
    }
    check = 0
    for name, user in gochiusa_bots.items():
        if user.voice.channel.id == channels[correct_channel[name]].id:
            check += 1
    
    if check >= 5:
        await ctx.send("太好了，就請你喝杯咖啡吧！")
        role = discord.utils.get(ctx.message.guild.roles, id=event_role_id)
        await ctx.author.remove_roles(role)
        for bot in gochiusa_bots.values():
            await bot.move_to(channels['machi'])
        await ctx.send("啊！怎麼又跑走了！真是的…")
    else:
        await ctx.send("好像還是哪裡怪怪的喔？")

client.run("Njk0NjY5MzE5ODc1MDY3OTA0.XoO_dw.SWV6x7ye9CxYpKSqwYf8xo7ywu4")