import random

player_wins = 0
computer_wins = 0
choices = ["rock", "paper", "scissors"]

# executes a best 2 out of 3 game of rock paper and scissors
while player_wins < 2 and computer_wins < 2:
  print("Let's play rock, paper, or scissors")

# takes and changes an input to lowercase so I can use == to compare inputs easier.
# also loops until given a valid input, which is cool.
  while True:
      player_choice = input("Choose wisely: ").lower()
      if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
        break
      
# computer "makes" its choice
  computer_choice = random.choice(choices) 
  print(f"Computer chooses {computer_choice}")

# compares the two choices and determines the winner
  if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
    winner = "Player"
  elif (player_choice == "rock" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "paper"):
    winner = "Tie"
  else:
    winner = "Computer"

# keeps track of and prints score
  if winner == "Player":
    player_wins += 1
    print("You won")
  elif winner == "Computer":
    computer_wins += 1
    print("Computer won")
  else:
    print("It's atie")
  print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")

# winner decided when player or computer wins reaches 2
if player_wins > computer_wins:
   print("Congratulations! You won.")
else:
   print("Computer won!")