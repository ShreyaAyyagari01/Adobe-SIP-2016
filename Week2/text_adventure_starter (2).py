start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
'''


print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("You decide to go left and find a monster. ") # finished the story by writing what happens
    user_input = input("Do you want to 'fight' or 'hide? ")
    if user_input == "fight":
    	print("Sorry, you are dead")
    elif user_input == "hide":
    	print("Success! The monster went away and you can see the exit! However, you are really tired...")
    	user_input = input("Do you chose to 'take a break' or 'continue'? ")
    	if user_input == "continue":
    		print("Sorry, you are dead")
    	elif user_input == "take a break"	
    		print("Congrats! You chose to take a quick break, and soon made it out of your way out of the maze!!!")


    #done = True
elif user_input == "right":
    print("You choose to go right and encounter a genie who offers to give you one free wish") # finished the story writing what happens
    user_input = input("Do you trust the genie? Type 'yes' or 'no': ")
    if user_input == "yes":
    	print("Sorry, the genie was a criminal, and you are dead")
    elif user_input == "no":
    	print("Success! You realize the genie was simply blocking the exit and was trying to trick you. You made it out of the maze!")
   # done = True
