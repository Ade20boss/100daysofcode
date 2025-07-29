import random
print("Welcome to rock, paper, scissors game!")
player_choice = input("Choose rock, paper, or scissors: ").lower()
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
if player_choice not in choices:
	print("Invalid choice. Please choose rock, paper, or scissors.")
else:
	if player_choice == computer_choice:
		print(f"Both players chose {player_choice}. It's a tie!")
	elif player_choice == "rock" and computer_choice == "scissors":
		print('''You choose:
		
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

''')
		print('''Computer choose:

		    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
		print(f"You chose {player_choice} and the computer chose {computer_choice}. You win!")
	elif player_choice == "paper" and computer_choice == "rock":
		print('''You choose:
		    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
		print('''Computer choose:
			    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) ''')
		print(f"You chose {player_choice} and the computer chose {computer_choice}. You win!")
	elif player_choice == "scissors" and computer_choice == "paper":
		print('''You choose:
			    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) ''')
		print('''Computer choose:
				    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) ''')
		print(f"You chose {player_choice} and the computer chose {computer_choice}. You win!")
	elif player_choice == "rock" and computer_choice == "paper":
		print('''You choose:
			
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
		print('''Computer choose:
			    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
		print(f"You chose {player_choice} and the computer chose {computer_choice}. You lose!")
	
	elif player_choice == "paper" and computer_choice == "scissors":
		print('''You choose:
		    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
		print('''Computer choose:
		    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')
		print(f"You chose {player_choice} and the computer chose {computer_choice}. You lose!")
	
	elif player_choice == "scissors" and computer_choice == "rock":
		print('''You choose:
				    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
		print('''Computer choose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')

		print(f"You chose {player_choice} and the computer chose {computer_choice}. You lose!")
				
