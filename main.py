import telebot

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

bot.polling()
