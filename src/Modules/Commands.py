import telebot
from src.Modules.User import User

class Commands:

    def start (bot, message):
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item = telebot.types.KeyboardButton("Compartir mi número", request_contact=True)
        markup.add(item)
        bot.reply_to(message, "¡Hola! Por favor, comparte tu número de teléfono.", reply_markup=markup)

    def add_contact (bot, number):
        User.setUser(number)

    def contacts (bot, message):
        USERS = User.getUsers()
        RETU_USERS = []
        for item in USERS:
            RETU_USERS.append(f"name: {item['name']} phone: {item['phone']}")

        PHRASE = "\n".join(RETU_USERS)

        bot.send_message(message.chat.id, PHRASE)