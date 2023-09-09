import time
import json

from src.configuration import PASSWORD, NUMBERS

AUTH = False

class Commands:

    def admin (bot, message):
        error_message = "Por favor, usa el comando /admin seguido de un parámetro válido."
        success_message = "Contraseña correcta.\nComandos:\n"

        commands="\n * /admin CONTRASEÑA \t ---> Autenticar admin \n * /add NÚMERO \t ---> Añadir nuevo contacto \n * /delete NÚMERO \t ---> Eliminar contacto \n * /list \t ---> Lista todos los contactos"

        try:
            comand, parameter =  message.text.split(" ", 1)
            global AUTH
            chat_id = message.chat.id
            if parameter == PASSWORD:
                AUTH = True
                bot.send_message(chat_id, success_message+commands,  parse_mode='HTML')
                time.sleep(60)
                AUTH = False
            else:
                bot.send_message(message.chat.id, error_message)
        except ValueError:
            bot.send_message(message.chat.id, error_message)

    def add_contact (bot, message):
        global AUTH

        if AUTH:
            FILE = {}
            with open('src/data/configuration.json', "r") as archivo:
                FILE = json.load(archivo)

            comand, NUMBER = message.text.split(" ", 1)
            FILE["NUMBERS"].append(NUMBER)

            with open('src/data/configuration.json', 'w') as file:
                json.dump(FILE, file, indent=4)

    def delete_contact (bot, message):
        global AUTH

        if AUTH:
            FILE = {}
            with open('src/data/configuration.json', "r") as archivo:
                FILE = json.load(archivo)
            comand, NUMBER =  message.text.split(" ", 1)
            if NUMBER in FILE["NUMBERS"]:
                FILE["NUMBERS"].remove(NUMBER)
                with open('src/data/configuration.json', 'w') as file:
                    json.dump(FILE, file, indent=4)

                bot.send_message(message.chat.id, "Contacto eliminado !!!")
            else:
                bot.send_message(message.chat.id, "Contacto no encontrado")

    def contacts (bot, message):
        global AUTH

        if AUTH:
            RETU_USERS = []

            for item in NUMBERS:
                RETU_USERS.append(f"- {item}")

            PHRASE = "\n".join(RETU_USERS)

            bot.send_message(message.chat.id, PHRASE)