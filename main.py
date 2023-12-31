import telebot
import json

from src.Modules.Interaction import Interaction
from src.Modules.Commands import Commands

FILE = {}
with open('src/data/configuration.json', "r") as archivo:
    FILE = json.load(archivo)

bot = telebot.TeleBot(FILE["ACCESS_TOKEN"])

#### Commands

@bot.message_handler(commands=['admin'])
def handle_admin(message):
    Commands.admin(bot, message)

@bot.message_handler(commands=['list'])
def handle_contacts(message):
    Commands.contacts(bot, message)

@bot.message_handler(commands=['add'])
def handle_add_contact(message):
    Commands.add_contact(bot, message)

@bot.message_handler(commands=['delete'])
def handle_delete_contact(message):
    Commands.delete_contact(bot, message)

@bot.message_handler(commands=['reset'])
def handle_add_contact(message):
    Commands.reset(bot, message)

### USUARIO

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if(message.text != FILE["PASSWORD"]):
        Interaction.identify_user(bot, message)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    Interaction.comprobe_number(bot, message)

bot.polling()
