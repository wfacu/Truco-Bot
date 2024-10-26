import discord
import datetime
from discord.ext import commands

@commands.command(name='ayuda', description='Muestra una guía instructiva del juego y de cómo funciona el bot.', aliases=['help', 'guide', 'guia', 'guía'])
async def ayuda(ctx):
    # Crear un embed
    embed = discord.Embed(
        title="Guía de ayuda y menú comandos",
        description="Truco es un appbot para jugar al _Truco argentino_ contra otro miembro del servidor.",
        color=discord.Color(0xB2C9E7),
    )

    # Añadir pie de página
    embed.set_footer(text="Programado por @wfacu", icon_url="https://i.ibb.co/YRgc2bX/github-brands-solid.png")
    embed.set_image(url="https://i.imgur.com/RehGhFA.png")

    # Añadir campos al embed
    embed.add_field(name="¿Cómo funciona?", value="Vas a poder iniciar una partida en cualquier canal de un servidor, pero las cartas que elijas para jugar solo las vas a poder ver vos únicamente, ya que el bot te manda tu mano de cartas por privado.\n\n" + 
    "Es importante por eso que tengas tus DMs habilitados, sino la partida no podrá iniciar.\n\n" +
    "El resultado de cada ronda y del final de la partida se muestra tanto en tus DMs como en el canal donde se inició la partida.\n\n" +
    "¡Ya lo sabes! Utiliza el comando `*comandos` para empezar a jugar.")

    embed.add_field(name="¿Cómo se juega?", value="**1.** Se reparten 3 cartas de manera aleatoria a cada jugador.\n\n"
    "**2.** El objetivo es ganar puntos jugando las cartas en diferentes rondas.\n\n"
    "**3.** Los jugadores pueden jugar una carta por turno y quien tenga la carta con más valor gana la ronda.\n\n"
    "**4.** El juego se continúa hasta que un jugador alcance el puntaje necesario para ganar la partida.")

    embed.add_field(name="Valores de las cartas", value="", inline=False)

    # Enviar el embed y la imagen
    await ctx.send(embed=embed)
