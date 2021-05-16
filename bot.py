import discord
from discord.ext import commands
import random

#mine
import getResponse
learntxt = []
i = 0
client = discord.Client()
token = "ODQzMzQzMzE1MDg0MTE1OTg5.YKCeqg.aHeSMYe1qxGiReLVUHQK21finuc"

bot = commands.Bot(command_prefix=':')
#getResponse.boot()

#runtime goes here
@client.event
async def on_message(message):
	global learntxt
	global i
	if message.author == client.user:
		return
	msg = message.content
	if msg.startswith(':help'):
		await message.channel.send("help and info = :help \n to get response = ; \n to end program = :::")

	if msg.startswith('---'):
		if learntxt == []:
			await message.channel.send("Later!")
			quit()
		getResponse.autoLearn(learntxt)
		getResponse.append(learntxt)
		

	if msg.startswith(';'):
		s = str(msg[2:])
		response = str(getResponse.getResponse(s))
		learntxt.append(s)
		learntxt.append(response)
		print(s)
		print(response)
		i += 1
		if i == 15:
			getResponse.autoLearn(learntxt)
			getResponse.append(learntxt)
			learntxt = []
			i = 0
		await message.reply(response)

client.run(token)