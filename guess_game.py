import random

x = random.randint(0,10)

while True:
	try:
		y = int(input('Enter a number'))
		if 0< y< 11:
			if y == x:
				print ("Hooray number guessed correctly")
				break
			else:
				print("Guess again")
	except ValueError:
		print("Need to enter a number")


