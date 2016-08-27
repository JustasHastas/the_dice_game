'''Algorith for playerTurn, program to play a 2-player dice game.
'''
import random
display_rule = "Player takes turns to throw dice. If the throw is a 'double', i.e. two 2s, two 3s, etc., the player's score reverts to zero and their turn ends. If the throw is not a 'double', the total shown on the two dice is added to the player's score. A player may have as many throws as they like in any turn until they either throw a double or pass the dice. The first player to reach a score of 50 wins the game."

def menuChoise():
	print("Option 1: Display rules")
	print("Option 2: Start new game")
	print("Option 3: Quit")
	choise = input()
	choise = int(choise)
	while choise <1 or choise >3:
		print("That is not a valid choise.")
		print("Please enter a number between 1 and 3")
		choise = input()
		choise = int(choise)
	return choise

# subroutine to display rules

def displayRules():
	print(display_rule)

# subroutine for each player to take a turn
def playerTurn(player, score):
	print("Your turn, ", player)
	anotherGo = "Y"
	scoreThisTurn = 0
	while anotherGo == "Y" or anotherGo == "y":
		die1 = random.randint(1, 6)
		die2 = random.randint(1, 6)
		print("You rolled ", die1,"and", die2)
		if die1 == die2:
			scoreThisTurn = 0
			cumulativeScore = 0
			print("Bad luck! Press any key to continue")
			anyKey = input() 	# accept any key press from user
			anotherGo = "N"
		else:
			scoreThisTurn = scoreThisTurn + die1 + die2
			cumulativeScore = score + scoreThisTurn
			print("Your score this turn is ", scoreThisTurn)
			print(player, "Your comulative score is", cumulativeScore)
			if cumulativeScore >= 50:
				anotherGo = "N"
			else:
				print("Another go? Answer Y or N")
				anotherGo = input()
	return cumulativeScore

# subroutine to play game
def playGame():
	score1 = 0
	score2 = 0
	print("Enter Player 1's name:")
	player1 = input()
	print("Enter Player 2's name:")
	player2 = input()
	while score1 < 50 and score2 < 50:
		score1 = playerTurn(player1, score1)
		print(score1)
		if score1 >= 50:
			print("You win!")
		else:
			score2 = playerTurn(player2, score2)
			if score2 >= 50:
				print("you win!")

# main program starts here
option = menuChoise()
while option != 3:
	print(option)
	if option == 1:
		displayRules()
	else:
		playGame()
	break
print("Goodbye!")
