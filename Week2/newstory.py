print("You wake up one morning and find that you are not in your bed; you are not even in your room.")
print("You are in the middle of a giant maze.")
print("A sign is hanging from the ivy: 'You have one hour. Don't touch the walls'")
print("There is a hallway to your right and to your left")




print("Type 'left' to go left or 'right' to go right.")
user_input = input()

while (user_input != "right" and user_input != "left"):
    print("Invalid response, try again: ")
    user_input = input()
   # break

if user_input == "left":
    print("You decide to go left and find a monster. ") # finished the story by writing what happens
    print("Do you want to 'fight' or 'hide?: ")
    user_input = input()
    while (user_input != "fight" and user_input != "hide"):
        print("Invalid response, try again: ")
        user_input = input()
        #break
    if user_input == "fight":
        print("Sorry, you are dead")
    elif user_input == "hide":
        print("Success! The monster went away and you can see the exit! However, you are really tired...")
        print("Do you chose to 'take a break' or 'continue'?: ")
        user_input = input()
        while (user_input != "take a break" and user_input != "continue"):
            print("Invalid response, try again: ")
            user_input = input()
           # break
        if user_input == "continue":
            print("Sorry, you are dead")
        elif user_input == "take a break":	
            print("Congrats! You chose to take a quick break, and soon made it out of your way out of the maze!!!")
        

            
    


    #done = True
elif user_input == "right":
    print("You choose to go right and encounter a genie who offers to give you one free wish") # finished the story writing what happens
    print("Do you trust the genie? Type 'yes' or 'no': ")
    user_input = input()
    while (user_input != "yes" and user_input != "no"):
        print("Invalid response, try again: ")
        user_input = input()
        #6break
    if user_input == "yes":
        print("Sorry, the genie was a criminal, and you are dead")
    elif user_input == "no":
        print("Success! You realize the genie was simply blocking the exit and was trying to trick you. You made it out of the maze!")



   # done = True