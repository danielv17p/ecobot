import discord
from discord.ext import commands,tasks
from juego import juegos
import asyncio
from PIL import Image, ImageDraw, ImageFont
import io

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@tasks.loop(hours=24)  # Se ejecutará cada 24 horas
async def daily_timer(channel):
    if channel:
        await channel.send("Este es tu recordatorio diario de reciclar!!")

@daily_timer.before_loop
async def before_daily_timer():
    print("Esperando que el bot esté listo para iniciar el temporizador...")
    await bot.wait_until_ready()  # Asegura que el bot esté completamente conectado antes de iniciar el temporizador

@bot.command()
async def timer(ctx):
    if not daily_timer.is_running():  # Verifica si el temporizador ya está corriendo
        await ctx.send("Temporizador de 24 horas iniciado.")
        daily_timer.start(ctx.channel)  # Inicia el temporizador en el canal actual
    else:
        await ctx.send("El temporizador ya está en ejecución.")

@bot.command()
async def stoptimer(ctx):
    if daily_timer.is_running():  # Verifica si el temporizador está corriendo
        daily_timer.cancel()  # Detiene el temporizador
        await ctx.send("El temporizador se detuvo.")
    else:
        await ctx.send("El temporizador no está en ejecución.")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'Ocurrió un error: {error}')
    print(f'Error en el comando: {error}')

@bot.command()
async def reciclaje(ctx):
    # Crear una imagen con fondo verde
    img = Image.new('RGB', (500, 250), color=(34, 177, 76))  # Color verde
    draw = ImageDraw.Draw(img)

    # Usar una fuente estándar
    font = ImageFont.load_default()

    # Escribir un mensaje en la imagen
    mensaje = "¡Recicla y cuida el planeta!"
    textwidth, textheight = draw.textsize(mensaje, font=font)
    position = ((img.width - textwidth) // 2, (img.height - textheight) // 2)

    # Escribir el texto en la imagen
    draw.text(position, mensaje, font=font, fill=(255, 255, 255))

    # Crear un archivo de imagen en memoria
    with io.BytesIO() as image_binary:
        img.save(image_binary, 'PNG')
        image_binary.seek(0)

        # Enviar la imagen al canal de Discord
        await ctx.send("Aquí tienes tu mensaje de reciclaje:", file=discord.File(fp=image_binary, filename='reciclaje.png'))    



@bot.command()
async def hello(ctx):
    await ctx.send("¡Hola! 🌍 Hoy puedes intentar reutilizar un frasco para organizar tus cosas. ¿Te animas? 🛠️ Si lo haces, comparte una foto y ganarás una medalla virtual. 🏅 ¡El planeta te lo agradecerá!")

@bot.command()
async def interesante(ctx):
    await ctx.send("¿Sabías que reciclar no solo ayuda al planeta, sino que también es una forma súper fácil de ser un héroe ambiental? 🌍 Cada botella de plástico que reciclas puede convertirse en algo nuevo, desde ropa hasta muebles. 🧴➡️🪑")

@bot.command()
async def soluciones(ctx):
    await ctx.send("puedes reutilizar tus cuadernos y darle un doble a las cosas y insistir a los demas a reutilizar")

@bot.command()
async def games(ctx):
    await ctx.send(juegos)

@bot.command()
async def opciones(ctx):
    await ctx.send("Reducir el uso de tu auto Utiliza el transporte público o camina o anda en bicicleta para trayectos cortos. Ahorrar agua Usa dos cubetas de agua para limpiar y enjuagar, y evita el desperdicio.  Apagar los dispositivos electrónicos Apaga los dispositivos cuando no los estés usando, como el celular o la computadora. ")

@bot.command()
async def joven(ctx):
    await ctx.send("Cerrar el grifo mientras te lavas los dientes, bañarte en 5 minutos, juntar el agua de la regadera mientras te bañas, son pequeñas acciones que ayudan a ahorrarla. Es importante separar los residuos en distintos botes: orgánica, vidrio, cartón, plásticos y desechos tóxicos.")

bot.run("token")