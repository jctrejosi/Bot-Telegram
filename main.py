import telebot

from src.Modules.Interaction import Interaction
from src.Modules.Commands import Commands
from src.Configuration import ACCESS_TOKEN

bot = telebot.TeleBot(ACCESS_TOKEN)

#### Commands

@bot.message_handler(commands=['start'])
def handle_start(message):
    Commands.start(bot, message)

@bot.message_handler(commands=['contacts'])
def handle_contacts(message):
    Commands.contacts(bot, message)

@bot.message_handler(commands=['add_contact'])
def handle_add_contact(message):
    Commands.add_contact(bot, message)

@bot.message_handler(commands=['delete_contact'])
def handle_delete_contact(message):
    Commands.delete_contact(bot, message)

@bot.message_handler(commands=['send_message'])
def handle_send_message(message):
    Commands.send_message(bot, message)

@bot.message_handler(commands=['reset'])
def handle_add_contact(message):
    Commands.reset(bot, message)

### USUARIO

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    Interaction.identify_user(bot, message)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    Interaction.comprobe_number(bot, message)

bot.polling()
