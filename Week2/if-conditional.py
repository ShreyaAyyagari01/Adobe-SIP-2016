number = 79
user_guess = input("Guess my lucky number: ")


while number != int(user_guess)
	if number < int(user_guess):
		print("Your guess was too high")
		user_guess = input("Try again: ")
	else number > int(user_guess):
		print("Your guess was too low")
		user_guess = input("Try again: ")

if number == int(user_guess):
	print("You got it right!!")

print("Game over")
