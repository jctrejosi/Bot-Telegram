import telebot
import time

from src.configuration import NUMBERS

class Interaction:

    def identify_user(bot, message):
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item = telebot.types.KeyboardButton("Compartir número", request_contact=True)
        markup.add(item)
        bot.reply_to(message, "¡Hola! Por favor, comparte tu número de teléfono.", reply_markup=markup)

    def comprobe_number(bot, message):
        phone_number = message.contact.phone_number
        number = phone_number[-10:]
        mensaje = "url (Se eliminará en 30s)"
        chat_id = message.chat.id

        message = bot.send_message(chat_id, mensaje)
        message_id = message.message_id

        if number in NUMBERS:
            time.sleep(60)
            bot.delete_message(chat_id, message_id)
        else:
            bot.send_message(message.from_user.id, f"No")