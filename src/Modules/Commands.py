import telebot
from src.Modules.Methods import Methods

class Commands:

    def start (bot, message):
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item = telebot.types.KeyboardButton("Compartir mi número", request_contact=True)
        markup.add(item)
        bot.reply_to(message, "¡Hola! Por favor, comparte tu número de teléfono.", reply_markup=markup)

    def add_contact (bot, message):
        NUMBER = message.text.split()[1:]
        SET_NUMBER = " ".join(NUMBER)
        Methods.setContact(int(SET_NUMBER))

    def delete_contact (bot, message):
        NUMBER = message.text.split()[1:]
        SET_NUMBER = " ".join(NUMBER)
        Methods.deleteContact(int(SET_NUMBER))

    def contacts (bot, message):
        USERS = Methods.getUsers()
        RETU_USERS = []
        for item in USERS:
            RETU_USERS.append(f"name: {item['name']} phone: {item['phone']}")

        PHRASE = "\n".join(RETU_USERS)

        bot.send_message(message.chat.id, PHRASE)