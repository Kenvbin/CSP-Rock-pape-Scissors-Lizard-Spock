#import functions
import random
import time

#make list for answers to randomise later
bot_answers = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

#welcome message
print("Welcome to Kevin's Rock Paper Scissors Lizard Spock Game.")
print("Type 'Stop' if you would like to quit at any time")
#ask for user input
player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")

#incase the user would instantly like to pause the program
if player_choice == "Stop":
  while player_choice == "Stop":
    break

#while loop incase user puts unkown Response
if player_choice != "Rock" and player_choice != "Paper" and player_choice != "Scissors" and player_choice != "Lizard" and player_choice != "Spock" and player_choice != "Stop":
  print("You did not write Rock, Paper, Scissors, Lizard or Spock. Try Again")
  player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")

#while loop to loop game untill the user asks to quit
while player_choice != "Stop":
  bot_choice = random.choice(bot_answers)

#Generating outcome
  if bot_choice == player_choice:
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Lizard")
    time.sleep(1)
    print("SPOCK")
    time.sleep(1)
    print("You Tied.")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")
  elif bot_choice == "Rock" and player_choice == "Paper":
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Lizard")
    time.sleep(1)
    print("SPOCK")
    time.sleep(1)
    print("You Win!")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")
  elif bot_choice == "Rock" and player_choice == "Scissors":
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Lizard")
    time.sleep(1)
    print("SPOCK")
    time.sleep(1)
    print("Sorry you lost.")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")
  elif bot_choice == "Rock" and player_choice == "Lizard":
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Lizard")
    time.sleep(1)
    print("SPOCK")
    time.sleep(1)
    print("Sorry you lost.")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")
  elif bot_choice == "Rock" and player_choice == "Spock":
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Lizard")
    time.sleep(1)
    print("SPOCK")
    time.sleep(1)
    print("You Win!")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")
  elif bot_choice == "Paper" and player_choice == "Rock":
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Lizard")
    time.sleep(1)
    print("SPOCK")
    time.sleep(1)
    print("Sorry you lost.")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")
  elif bot_choice == "Paper" and player_choice == "Scissors":
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Lizard")
    time.sleep(1)
    print("SPOCK")
    time.sleep(1)
    print("You Win!")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")
  elif bot_choice == "Paper" and player_choice == "Lizard":
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Lizard")
    time.sleep(1)
    print("SPOCK")
    time.sleep(1)
    print("You Win!")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")
  elif bot_choice == "Paper" and player_choice == "Spock":
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Lizard")
    time.sleep(1)
    print("SPOCK")
    time.sleep(1)
    print("Sorry you lost.")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")
  elif bot_choice == "Scissors" and player_choice == "Paper":
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Lizard")
    time.sleep(1)
    print("SPOCK")
    time.sleep(1)
    print("Sorry you lost.")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")
  elif bot_choice == "Scissors" and player_choice == "Rock":
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Lizard")
    time.sleep(1)
    print("SPOCK")
    time.sleep(1)
    print("You Win!")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")
  elif bot_choice == "Scissors" and player_choice == "Lizard":
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Lizard")
    time.sleep(1)
    print("SPOCK")
    time.sleep(1)
    print("Sorry you lost.")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")
  elif bot_choice == "Scissors" and player_choice == "Spock":
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Lizard")
    time.sleep(1)
    print("SPOCK")
    time.sleep(1)
    print("You Win!")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")
  
  #while input in loop so then if unknown response
  while player_choice != "Rock" and player_choice != "Paper" and player_choice != "Scissors" and player_choice != "Lizard" and player_choice != "Spock" and player_choice != "Stop":
    print("You did not write Rock, Paper, Scissors, Lizard or Spock. Try Again")
    player_choice = input("Select Rock, Paper, Scissors, Lizard or Spock!: ")

#a goodbye message for whenever the user wants to leave
print("Goodbye thanks for playing Rock, Paper, Scissors, Lizard Spock!")
while player_choice == "Stop":
  break