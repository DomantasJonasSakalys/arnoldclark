import random

#The following describe the basic rules and selections. Key beats Values.
rules = {
'Rock' : ['Lizard', 'Scissors'],
'Paper' : [ 'Rock', 'Spock'],
'Scissors' : [ 'Paper', 'Lizard' ], 
'Lizard' : ['Spock', 'Paper'],
'Spock' : ['Scissors', 'Rock']
}

#Making selections from the keys
selections =  ', '.join(list(rules.keys()))

def run():
	#Selection statement
	print('\nTo play enter one of the selections:\n' + selections)

	#Player selection
	player = input('You choose: ').capitalize()
	
	#Check for valid input
	while player not in rules.keys():
		print('\nInvalid input, try again\n')
		player = input('You choose: ').capitalize()
	
	#AI selection
	ai = random.choice(list(rules.items()))[0]
	print('AI selected: ' + str(ai))

	#Check and tell who won
	if ai in rules[player]:
		print('You Won, ' + player + ' beats ' + ai)
		return 1
	elif player in rules[ai]:
		print('You Lost, ' + ai + ' beats ' + player)
		return 2
	else:
		print("It's a Tie")
		return 3

#Start the game
print('Welcome to the '+ selections + ' game!')
run()
#Play again?
while input('Play again? ').capitalize()[0:1] == 'Y':
	run()
exit()
