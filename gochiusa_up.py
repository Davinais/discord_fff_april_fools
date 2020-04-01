from discord.ext import commands
import asyncio
import configparser

lize = commands.Bot(command_prefix='++')
chino = commands.Bot(command_prefix='++')
kokoa = commands.Bot(command_prefix='++')
syaro = commands.Bot(command_prefix='++')
chiya = commands.Bot(command_prefix='++')

lize.load_extension('cmd')
chino.load_extension('cmd')
kokoa.load_extension('cmd')
syaro.load_extension('cmd')
chiya.load_extension('cmd')

config = configparser.ConfigParser()
config.read('gochiusa.ini')

loop = asyncio.get_event_loop()
loop.create_task(lize.start(config['tokens']['lize']))
loop.create_task(chino.start(config['tokens']['chino']))
loop.create_task(kokoa.start(config['tokens']['kokoa']))
loop.create_task(syaro.start(config['tokens']['syaro']))
loop.create_task(chiya.start(config['tokens']['chiya']))

try:
    loop.run_forever()
except KeyboardInterrupt as e:
    loop.stop()
    loop.close()
    print("\nFinished!")
