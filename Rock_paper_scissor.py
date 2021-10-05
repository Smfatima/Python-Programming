from random import randint

choices = ["rock", "paper", "Scissors"]


computer = choices[randint(0, 2)]

print("Welcome to the game Rock, Paper, Scissors")

player = input("Your choice: ").lower()
print("computer choice "+computer)

if player == computer:
    print("Draw")
elif player == "rock" and computer == "paper":
    print("Computer Wins")
elif player == "rock" and computer == "scissors":
    print("Player wins")
elif player == "paper" and computer == "rock":
    print("Player wins")
elif player == "paper" and computer == "scissors":
    print("Computer wins")
elif player == "scissor" and computer == "rock":
    print("Computer wins")
elif player == "Scissors" and computer == "paper":
    print("Players wins")
