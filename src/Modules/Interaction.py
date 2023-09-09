import telebot
import time
import json
import datetime

class Interaction:

    def identify_user(bot, message):
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item = telebot.types.KeyboardButton("Compartir número", request_contact=True)
        markup.add(item)
        bot.reply_to(message, "¡Hola! Por favor, comparte tu número de teléfono.", reply_markup=markup)

    def comprobe_number(bot, message):
        phone_number = message.contact.phone_number
        number = phone_number[-10:]
        chat_id = message.chat.id
        contact = message.contact

        fecha_actual = datetime.datetime.now()

        user_list = []
        with open('src/data/history.json', "r") as archivo:
            user_list = json.load(archivo)

        user_data = {
            'date': fecha_actual.strftime("%d/%m/%Y %H:%M"),
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'phone_number': contact.phone_number,
            'user_id': contact.user_id,
            'username': message.from_user.username
        }

        user_list.append(user_data)

        with open('src/data/history.json', 'w') as file:
            json.dump(user_list, file, indent=4)

        NUMBERS = []
        with open('src/data/configuration.json', "r") as archivo:
            NUMBERS = json.load(archivo)["NUMBERS"]

        if (number in NUMBERS):
            message = bot.send_message(chat_id, "url (Se eliminará en 30s)")
            message_id = message.message_id
            time.sleep(30)
            bot.delete_message(chat_id, message_id)
        else:
            bot.send_message(chat_id, "No tiene permiso")