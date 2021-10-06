import os,discord,asyncio,datetime,traceback,json
from discord.ext import commands, tasks
from get_news import get_news
from replit import db
from json import JSONEncoder
from news_class import dictToNews

#Cria uma classe para permitir que as instâncias de News sejam serializadas
class NewsEncoder(JSONEncoder):
	def default(self,o):
		return o.__dict__

bot = commands.Bot(command_prefix="&", intents=discord.Intents.all())

#Carrega da memória as notícias já enviadas
newsfile = open('current_news.json',"r")
current_news_dict = json.load(newsfile)
current_news={}
for k in current_news_dict:
	l=[]
	for e in current_news_dict[k]:
		l.append(dictToNews(e))
	current_news[k]=l
newsfile.close()

async def send_news(n,guild):
	embed = discord.Embed(
		colour = discord.Colour.dark_gold(),
		title = n.title,
		description = n.description,
		url = n.link
	)
	embed.set_image(url=n.thumbnail)
	channels = guild.text_channels
	for channel in channels:
		if channel.is_news():
			await channel.send(embed = embed)
	

@tasks.loop(hours=1)
async def update_news():
	for guild in bot.guilds:
		cnews_guild = current_news.get(str(guild.id))
		try:
			news = get_news(db[str(guild.id)])
		except Exception as e:
			print(type(e))
			traceback.print_exc()
		updated=True
		for n in news:
			if cnews_guild:
				verification = n not in cnews_guild
				if verification:
					updated=False
					await send_news(n,guild)
			else:
				try:
					updated=False
					await send_news(n,guild)
				except Exception as e:
					print(e)
					print(type(e))
					traceback.print_exc()

		if not updated:
			current_news[str(guild.id)] = news
			newsfile = open("current_news.json",'w')
			json.dump(current_news,newsfile,indent=6,cls=NewsEncoder)
			newsfile.close()

#Verifica quanto tempo até a próxima hora completa e dorme o loop até a mesma
@update_news.before_loop
async def looper():
	delta = datetime.timedelta(hours=1)
	now = datetime.datetime.now()
	next_hour = now+delta
	await asyncio.sleep((next_hour-now).seconds)

@bot.event
async def on_ready():
	print(f"Bot iniciado como: {bot.user}")

@bot.event
async def on_guild_join(guild):
	sys_channel = guild.system_channel
	db[guild.id] = "caruaru"
	if sys_channel:
		try:
			await sys_channel.send("Utilize o comando \"&alterarcampus (seucampus)\" para definir de qual campi as notificações serão enviadas!")
		except Exception as e:
			print(f"!!Não foi possível solicitar definição de campus no servidor: {guild.name}!!\nError:{e}\n\n")

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def alterarcampus(ctx,campus):
	db[ctx.guild.id] = str(campus)
	await ctx.channel.send(f"Campus alterado com sucesso para {campus}")

@alterarcampus.error
async def alterarcampus_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        msg = "Você não tem permissão para executar essa ação, peça à um administrador!"  
        await ctx.send(msg)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def atualizarmanual(ctx):
	guild_id = ctx.guild.id
	cnews_guild = current_news.get(str(guild_id))
	try:
		news = get_news(db[str(guild_id)])
	except Exception as e:
		print(type(e))
		traceback.print_exc()
	updated=True
	for n in news:
		if cnews_guild:
			verification = n not in cnews_guild
			if verification:
				updated=False
				await send_news(n,ctx.guild)
		else:
			try:
				updated=False
				await send_news(n,ctx.guild)
			except Exception as e:
				print(e)
				print(type(e))
				traceback.print_exc()

	if not updated:
		current_news[str(guild_id)] = news
		print(f"Manually updated by: {ctx.author}\n{datetime.datetime.now()}\n")
		try:
			newsfile = open("current_news.json",'w')
			json.dump(current_news,newsfile,indent=6,cls=NewsEncoder)
			await ctx.send("As notícias foram atualizadas com sucesso!")
		except Exception as e:
			print(e)
			print(type(e))
			traceback.print_exc()
	else:
		await ctx.send("Notícias já atualizadas!")


@atualizarmanual.error
async def atualizarmanual_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        msg = "Você não tem permissão para executar essa ação, peça à um administrador!"  
        await ctx.send(msg)

update_news.start()
bot.run(os.environ['DISCORD-BOT-TOKEN'])