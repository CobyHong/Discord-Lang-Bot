#Bot by Coby Hong using discord.py and free google translate API for Python.
#Welcome to edit and use code as long as some form of credit is given.

#GITHUB:	https://github.com/CobyHong
#Website:	www.coby.tech
#Email:		CobyHong@gmail.com

# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhyyyyyhhhysssssssyhhhhhhh
# hhhhhhysssyhhhssssssssyhhhhhhh
# hhhhhhs///shhhssssssssyhhhhhhh
# hhhhhho:::shhhssssssssyhhhhhhh
# hhhhhho:::shhh////////ohhhhhhh
# hhhhhho:::shhh////////ohhhhhhh
# hhhhhho:::shhh////////ohhhhhhh
# hhhhhho:::osss////////oyhhhhhh
# hhhhhho:::+ooooooooooooyhhhhhh
# hhhhhho::::::::::::::::ohhhhhh
# hhhhhhs++++++++++++++++shhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio 
from googletrans import Translator
import languages

#Turning language array into printable list for later use.
options = []
for i in languages.LANGUAGES:
	options.append(i[0] + " : " + i[1])

#Setting default prefix for commands
bot = commands.Bot(command_prefix="!")
translator = Translator()

#Print statements to command prompt showing bot has successfully joined server.
@bot.event
async def on_ready():
	print("Lang Bot is ONLINE!")
	print("Bot's name on server '" + bot.user.name + "' with ID:" + bot.user.id)
	print("\n@GITHUB:\thttps://github.com/CobyHong\n@Website:\twww.coby.tech\n@Email:\t\tCobyHong@gmail.com")
	print("GOOD")

#command functions
@bot.event
async def on_message(message):
	for i in languages.LANGUAGES:
		if message.content.startswith("!{} ".format(i[0])):
			#removes command portion to user's message
			msg = message.content.replace("!" + i[0], "")
			#detects language of user to convert labeling to their language. CURRENTLY NOT IN USE.
			detected_language = translator.detect(msg).lang
			embed = discord.Embed(color=0xff9b72)
			#labels and translations on second embed.
			embed.add_field(name="__{}__:".format(message.author), value='"'+msg+' "', inline=True)
			embed.add_field(name=":arrow_down:", value=translator.translate('"'+msg+' "', dest= i[0]).text, inline=True)
			await bot.send_message(message.channel, embed=embed)
	
	#ping function to see if bot is online
	if message.content.startswith("!status"):
		await bot.send_message(message.channel, "Hello **{}**! We are live! :earth_americas:".format(message.author))

	#list of languages
	if message.content.startswith("!lang"):
		await bot.send_message(message.author, "**__These are all the available languages with command suffixes__**\n\n" + '\n'.join(options))

	#list of languages
	if message.content.startswith("!about"):
		await bot.send_message(message.author, "Hello, my name is Coby.\nI'm a sad Asian kid who got bored one summer night and made this. \n\nHere's my website:	www.coby.tech")

#Running bot off this token ID
bot.run("NDYzMjAyNDI0NTkzODQyMTg3.DhtD8g.3nIbn6ZMhEuZKNgjb57gE9iE790")