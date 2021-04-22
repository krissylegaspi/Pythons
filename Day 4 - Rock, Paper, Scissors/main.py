import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
print(game_images[userChoice])
computerChoice = random.randint(0, 2)
print("Computer chose: " + game_images[computerChoice])

if (userChoice >= 3) or (userChoice < 0):
    print("You typed an invalid number, you lose!")
elif (userChoice == 0) and (computerChoice == 2):
    print("You win!")
elif (userChoice == 2) and (computerChoice == 0):
    print("You lose!")
elif (computerChoice > userChoice):
    print("You lose!")
elif (userChoice > computerChoice):
    print("You win!")
elif (computerChoice == userChoice):
    print("It's a tie!")

'''
if (userChoice == 0) and (computerChoice == 2):
    print(rock)
    print("Computer chose: \n" + scissors)
    print("You win!")
elif (userChoice == 1) and (computerChoice == 2):
    print(paper)
    print("Computer chose: \n" + scissors)
    print("You lose!")
elif (userChoice == 2) and (computerChoice == 2):
    print(scissors)
    print("Computer chose: \n" + scissors)
    print("It's a tie!")
elif (userChoice == 0) and (computerChoice == 1):
    print(rock)
    print("Computer chose: \n" + paper)
    print("You lose!")
elif (userChoice == 1) and (computerChoice == 1):
    print(paper)
    print("Computer chose: \n" + paper)
    print("It's a tie!")
elif (userChoice == 2) and (computerChoice == 1):
    print(scissors)
    print("Computer chose: \n" + paper)
    print("You win!")
elif (userChoice == 0) and (computerChoice == 0):
    print(rock)
    print("Computer chose: \n" + rock)
    print("It's a tie!")
elif (userChoice == 1) and (computerChoice == 0):
    print(paper)
    print("Computer chose: \n" + rock)
    print("You win!")
elif (userChoice == 2) and (computerChoice == 0):
    print(scissors)
    print("Computer chose: \n" + rock)
    print("You lose!")
else:
    print("Invalid number. Try again.\n")
'''