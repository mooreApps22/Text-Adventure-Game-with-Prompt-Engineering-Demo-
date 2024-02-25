import os
from anthropic import Anthropic

class MyClass:

	my_attribute = "This is a class atrribute"
	def __init__(self, name):
		self.name = name

	def say_hello(self):
		return f"Hello {self.name}!"


"""
API_KEY="XXX"
client = Anthropic(api_key=API_KEY)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Pretent you are a girl named Alice. And saying something about your day.",
        }
    ],
    model="claude-2.1",
)
"""

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
    return message.content

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



print("Welcome to the The Game")
next_message("This a customisable migration game, that allows you to pick the any group in history.")

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
	print(response) 

#claude_acting('Pretend you are' + people + ' and saying goodbye, in English, to some of your friends who are about to migrate to ' + dest  + ' in ' + year  + ', in two english sentences.')




claude_acting('''You will pretend to be a <people>{{'''+ people +'''}}</people> person in <year>{{'''+ year +'''}}</year>. You will say two short sentences to your friends who are about to embark on a journey to <destination>{{'''+ dest +'''}}</destination>.

Here are some important rules for the interaction:

-Always stay in character.
- If you are unsure how to respond, say "Sorry, I didn\'t understand that. Could you rephrase your question?"

Please respond to the user’s questions within <response></response> tags.''')

next_message(' ')
