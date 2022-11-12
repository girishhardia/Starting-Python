import random
user_input = input("Enter a choise: (rock, paper or scissors)  ")
possible_actions = ["rock", "paper","scissors"]
computer_action = random.choice(possible_actions)

print("Computer chose",computer_action)

if user_input==computer_action:
    print("Draw")
elif user_input == "rock" and computer_action == "paper":
    print("You Lose")
elif user_input == "rock" and computer_action == "scissors":
    print("You Won")
elif user_input == "paper" and computer_action == "rock":
    print("You Won")
elif user_input == "paper" and computer_action == "scissors":
    print("You Lose")
elif user_input == "scissors" and computer_action == "rock":
    print("You Lose")
elif user_input == "scissors" and computer_action == "paper":
    print("You Won")
