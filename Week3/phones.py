#attr: type, size, color
#methods: call, text, play games, take pictures

class phone():
    def __init__(self, typeOfPhone, size, color, brand,gender):
        self.typeOfPhone = typeOfPhone
        self.size = size
        self.color = color
        self.brand = brand
        self.gender = gender
        self.pronoun = "they"

    #methods
    def call(person):
        print("You are calling " +person+ " from your " + self.brand + ", " + self.color+ " phone.")

    def  playGames(game):
        print("You are currently playing " +game ".")

    def pronouns():
        if (self.gender == "female"):
            return self.pronoun = "she"
        elif (self.gender == "male"):
            return self.pronoun = "he"
        return self.pronoun



