import discord
from discord.ext import commands
import secrets
from comandos.ayuda import ayuda

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)

# Log in #
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.CustomActivity(name="Utiliza el comando *menu"))
    print(f'\n¡Conectado al cliente como {bot.user}!')

# Deshabilitar el comando help por defecto
bot.remove_command('help')

# Registrar comandos
bot.add_command(ayuda)

# Run bot
bot.run(secrets.TOKEN)
