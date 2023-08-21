#### Dependencies

import telebot

#### Modules

from Commands import Commands

COMMANDS = Commands("Juan")

ACCESS_TOKEN = "5792500803:AAEl4kkgK3QHEjKZrM1CidSrVL4J94R5k20"

bot = telebot.TeleBot(ACCESS_TOKEN)

#### Manejador de inicio

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    item = telebot.types.KeyboardButton("Compartir mi número", request_contact=True)
    markup.add(item)
    bot.reply_to(message, "¡Hola! Por favor, comparte tu número de teléfono.", reply_markup=markup)

#### Contactos
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    user_phone = message.contact.phone_number
    bot.reply_to(message, f"Gracias por compartir tu número: {user_phone}")

#### Conversación

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower() == 'hola':
        bot.reply_to(message, "¡Hola! ¿En qué puedo ayudarte?")
    elif message.text.lower() == 'adios':
        bot.reply_to(message, "¡Hasta luego! Si necesitas algo más, aquí estaré.")
    else:
        bot.reply_to(message, "No entiendo ese mensaje. Prueba con 'hola' o 'adios'.")

bot.polling()
