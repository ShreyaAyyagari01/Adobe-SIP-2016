class Dog():

    #Constructor Function
    def __init__(self, color, weight, eyeColor, name):
            self.color = color
            self.weight = weight
            self.eyeColor = eyeColor
            self.name = name

    def bark(self):
        print("Woof")

    def wag(self):
        print("Wagging Tail")
    def run(self):
        print("Your dog is running")

Toto = Dog("Brown", 25, "Blue", "Toto")

Toto.run()