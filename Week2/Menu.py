import random
adjective_1 = ["Crispy", "Crunchy", "Cool", "Salted", "Fresh", "Light", "Minty", "Tender", "Smooth", "Spicy"]
adjective_2 = ["Fried", "Seasoned", "Toasted", "Spongy", "Roasted", "Infused", "Garlicky", "Buttered", "Stuffed", "Glazed"]
food_1 = ["Vegetables", "Noodles", "Chicken", "Marshmallows", "Peanuts", "Potatoes", "Cake", "Bread", "Macaroni", "Apples"]




for i in range(10):
    
    random_integer1 = random.randint(0, len(adjective_1)-1)
    random_integer2 = random.randint(0, len(adjective_2)-1)
    random_integer3 = random.randint(0, len(food_1)-1)



    print( adjective_1[random_integer1] + " " + adjective_2[random_integer2] + " " + food_1[random_integer3])
    del adjective_1[random_integer1]
    del adjective_2[random_integer2]
    del food_1[random_integer3]

user_guess = input("Guess a letter")

if 
    
