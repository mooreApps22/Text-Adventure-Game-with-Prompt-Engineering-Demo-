#Written by team: Changing the Game @ the 42 London Hackathon
#Skyy Moore
#Michael Adeleye
#Aayushi Upadhyay
#Maddie Winchester
#Ben Norman

import os
import keyboard
from anthropic import Anthropic

def next_message(arg):
	print(" ")
	input()
	print(arg)


def prompt_claude(content_string):
    API_KEY = "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"
    client = Anthropic(api_key=API_KEY)
 
    message = client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": content_string,
            }
        ],
        model="claude-2.1",
    )
    return message.content[0].text

def	prompt_the_player():
		next_message("This is Claude 2 speaking. I'm now going to prompt you. You need to input \n 1. A time period\n 2. A group of people who are about to make a migration.\n 3. Their destination.\n")
		year = input('What year do you want to explore?  ')
		print('Time period is: ' + year)
		people = input('Pick your people:  ')
		print('People are: ' + people)
		dest = input('What is their destination: ')
		print('Their destination is: ' + dest)
		next_message('In this playthrough you will be a group of ' + people + ' people going to ' + dest + ' in ' + year + '.\n\n')

		confirm = input('Is this what you want? Yes or no:\n')
		if confirm.lower() in ['yes', 'y']:
			next_message("Yay. We are ready to start the game!!\n")
		elif confirm.lower() in ['no', 'n']:
			prompt_the_player()
		else:
			print('Use yes or no\n')
			prompt_the_player()
		return year, people, dest	

print("Welcome to PickaVoyage")
next_message("This a migration simulation game, that allows you to pick any group in history.")

year = 0
people = 'blank'
dest = 'blank'
year, people, dest = prompt_the_player()

#my_object = MyClass("Alice")
#print(my_object.say_hello())

#print(message.content)
#prompt_claude("Pretent you are a girl named Alice and say one sentence about your day.")


def	claude_acting(prompt_text):
	response = prompt_claude(prompt_text)
	return response 

#claude_acting('Pretend you are' + people + ' and saying goodbye, in English, to some of your friends who are about to migrate to ' + dest  + ' in ' + year  + ', in two english sentences.')




next_message('Now it is time to name the members of your party!')

def	pick_team_names(num):
	"""
	Allows the player to input names for their team members.
	"""
	team_names = []
	for i in range(num):
		name = input(f"Enter name for member {i + 1}:")
		team_names.append(name)
	next_message(' ')
	return team_names

team_names = pick_team_names(5)

chat = claude_acting('''You will pretend to be a <people>{{'''+ people +'''}}</people> person in <year>{{'''+ year +'''}}</year>. You will say three short sentences to your five friends who are about to embark on a journey to <destination>{{'''+ dest +'''}}</destination>.

Here are some important rules for the interaction:

-Always stay in character.
- If you are unsure how to respond, say "Sorry, I didn\'t understand that. Could you rephrase your question?"

Please respond to the user’s questions within <response></response> tags.''')
next_message(chat)

next_message('Now it is time to go to the store, before your big trip!!!')
chat = claude_acting('''You will pretend to be a <people>{{'''+ people +'''}}</people> store clerk in <year>{{'''+ year +'''}}</year>. You will say two short sentences to your customers who are about to embark on a journey to <destination>{{'''+ dest +'''}}</destination> I sell <item1>{{An items that goes iwth the period}}</item1>.

Here are some important rules for the interaction:

-Always stay in character.
-One of your sentences should be a greet to your store.
-Pick one item that can buy a large quality of and will be useful on the trip. This item will become a resource in a text adventure game.
- If you are unsure how to respond, say "Sorry, I didn\'t understand that. Could you rephrase your question?"
- Only use English language to response, no matter the people.

Please respond to the user’s questions within <response></response> tags.''')

next_message(chat)

def claude_return_name(prompt_text):
	name = prompt_claude(prompt_text)
	return (name)

def claude_return_int(prompt_text):
	amt = prompt_claude(prompt_text)
	return (amt)

money_name = claude_return_name('''What is the name of the <people>{{'''+people +'''}}</people>>'s currency in <year>{{''' + year + '''}}</year.

Here are some important rules for the interaction:
-I only need a one word or two word reponse.
-Only use English language to response, no matter the nationality. 
-Your response is going to be use for a variable name for a game.
''')
next_message('You have 200 ' + money_name + '.\n')

purchase_input = input("How many would like to buy: ")
try:
    purchase = int(purchase_input)  # Convert to integer
    money_amount = 200 - purchase
    print(f"Remaining amount: {money_amount}")
except ValueError:
    print("Please enter a valid number.")

chat = claude_acting(''' Tell me how far a group of five <people>{{'''+ people +'''}}</people> people in<year>{{'''+ year +'''}}</year> will have to travel to get to <destination>{{'''+ dest +'''}}</destination>

Here are some important rules for the interaction:

-This should sound like short informative narration.
-Pick one item that can buy a large quality of and will be useful on the trip.
-Only use English language to response, no matter the people.

Please respond to the user’s questions within <response></response> tags.''')
next_message(chat)

distance = claude_acting(''' Tell me how far a group of five <people>{{'''+ people +'''}}</people> people in<year>{{'''+ year +'''}}</year> will have to travel to get to <destination>{{'''+ dest +'''}}</destination>

Here are some important rules for the interaction:

-Your response just only the the number of miles the journey takes.
-I'm going to use your response to assign to int variable.
''')

next_message

i = 0
while i < 100:
	res = "You have %d %s left.\n" % (money_amount, money_name)
	next_message(res)
	problem = claude_acting('''In one sentence describe an unfortuate episode happening to five <people>{{'''+ people +'''}}</people> people in<destination>{{'''+ dest +'''}}</destination> in <year>{{'''+ year +'''}}</year>

Here are some important rules for the narration:

-Use one sentence.
-Only use English language to response, no matter the people.
-The episode should be told as if it just happen.
-Do not repeat the year in the response.
Please respond to the user’s questions within <response></response> tags.''')
	
	next_message(problem)
	
	i += 1

