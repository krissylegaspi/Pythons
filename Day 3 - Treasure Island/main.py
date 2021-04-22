firstStep = input('Welcome to Treasure Island. \nYour mission is to find the treasure. \nYou\'re at a cross road. Where do you want to go? Type "left" or "right"\n')

if (firstStep == "left"):
    secondStep = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if (secondStep == "wait"):
        thirdStep = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n')
        if (thirdStep == "red"):
            print("You were burned by fire. Game Over.")
        elif (thirdStep == "blue"):
            print("You were eaten by beasts. Game Over.")
        elif (thirdStep == "yellow"):
            print("You Win! Congratulations.")
        else:
            print("Game Over.")
    else:
        print("You were attacked by a swarm of trouts. Game Over.")
else:
    print("You fell into a hole. Game Over.")