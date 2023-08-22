import json

class Methods:

    def setContact (number):
        try:
            with open("src/data/numbers.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return []

        data.append(number)

        with open("src/data/numbers.json", "w") as file:
            json.dump(data, file, indent=2)

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

