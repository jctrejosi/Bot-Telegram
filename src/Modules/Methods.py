import json
from src.configuration import PASSWORD, NUMBERS

class Methods:

    def setContact (number):
        NUMBERS.append(number)

    def deleteContact (number):
        try:
            with open("src/data/numbers.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return []

        index = data.index(number)
        data.pop(index)

        with open("src/data/numbers.json", "w") as file:
            json.dump(data, file, indent=2)

    def getUsers ():
        try:
            with open("src/data/users.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return []

        return data

    def comrobePassword (bot, message):
        bot.send_message(message.chat.id, "Contraseña:")
        if PASSWORD == message.text: return True
        return False
