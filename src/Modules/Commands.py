import time
import json
import re

AUTH = False

FILE = {}
with open('src/data/configuration.json', "r") as archivo:
    FILE = json.load(archivo)

def validar_numero(numero_str):
    patron = r'^\d{10}$'
    if re.match(patron, numero_str):
        return True
    else:
        return False

class Commands:

    def admin (bot, message):
        error_message = "Por favor, usa el comando /admin seguido de un parámetro válido."
        success_message = "Contraseña correcta.\nComandos:\n"

        commands="\n * /admin contraseña \t // Autenticar admin \n * /add número \t // Añadir nuevo contacto (ej: /add 1234567890) \n * /delete número (ej: /delete 1234567890) \t // Eliminar contacto \n * /list \t // Lista todos los contactos"

        try:
            comand, parameter =  message.text.split(" ", 1)
            global AUTH
            global FILE

            chat_id = message.chat.id
            if parameter == FILE["PASSWORD"]:
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
            if NUMBER not in FILE["NUMBERS"]:
                if validar_numero(NUMBER):
                    FILE["NUMBERS"].append(NUMBER)

                    with open('src/data/configuration.json', 'w') as file:
                        json.dump(FILE, file, indent=4)
                else:
                    bot.send_message(message.chat.id, "El contacto no es válido")
            else:
                bot.send_message(message.chat.id, "Ya existe este contacto")

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

            NUMBERS = []
            with open('src/data/configuration.json', "r") as archivo:
                NUMBERS = json.load(archivo)["NUMBERS"]

            for item in NUMBERS:
                RETU_USERS.append(f"- {item}")

            PHRASE = "\n".join(RETU_USERS)

            bot.send_message(message.chat.id, PHRASE)