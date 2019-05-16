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
selections = ''
for rule in rules.keys():
	selections += rule + ', '
selections = selections[0:-2]

def run():
	#Selection statement
	print('\nTo play enter one of the selections:\n' + selections)

	#Opponent selections
	player = input('You choose: ').capitalize()
	ai = random.choice(list(rules.items()))[0]
	
	#Check for valid input
	while player not in rules.keys():
		print('\nInvalid input, try again\n')
		player = input('You choose: ').capitalize()
	print('AI selected: ' + str(ai))

	#Check and tell who won
	if ai in rules[player]:
		print('You Won, ' + player + ' beats ' + ai)
	elif player in rules[ai]:
		print('You Lost, ' + ai + ' beats ' + player)
	else:
		print('Tie, ' + player + " doesn't do anything to " + ai)
	
	#Play again?
	if input('Play again?(y?)').capitalize() == 'Y':
		run()
	exit()

#Start the game
print('Welcome to the '+ selections + ' game!')
run()
