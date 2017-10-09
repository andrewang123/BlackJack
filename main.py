import sys #user input
import random
from random import randint
#gets the users name
def getUserName():
    name = input('What is your name? ')
    print("Hello", name)
    choice = input("Would you like to play Black Jack? (1 yes, 2 no)")
    choice = int(choice)#convert to a int

    while choice not in (1, 2):
        print("not valid number try again")
        choice = input()
        choice = int(choice)  # convert to a int
    if choice == 1:
        print("Ok cool, let us get started")
    elif choice == 2:
        print("Ok... maybe some other time...")
        exit()
    return name

#define the rules of blackjack
def rules():
    print("1. Get 21 points on the player's first two cards " 
          " (called a \"blackjack\" or \"natural\"),\n" \
                        "without a dealer blackjack;")
    print("2. Reach a final score higher than the "
          "dealer without exceeding 21")
    print("3. Let the dealer draw additional "
          "cards until their hand exceeds 21. ")
def playGame(userName):
    cards= [1,2,3,4,5,6,7,8,9,10,11,12,13] # Ace = 1 or 11, J=11, Q=12, K=13
    userCardOne = random.randint(1,13)
    userCardTwo = random.randint(1,13)
    compCardOne = random.randint(1,13)
    compCardTwo = random.randint(1,13)

    # cards before conversion
    print(userName, "your two cards are: ", userCardOne, "and", userCardTwo)
    print("Computer Cards are ", compCardOne, "and", compCardTwo)
    #Convert all of the jacks, queens and kings to 10s
    if userCardOne in(11, 12,13):
        userCardOne = 10
    if userCardTwo in(11,12,13):
        userCardTwo = 10
    if compCardOne in(11,12,13):
        compCardOne = 10
    if compCardTwo in (11,12,13):
        compCardTwo = 10

    # ask if user wants to change ace to 11
    if(userCardOne == 1):
        print("Do you want to change the value of Ace to 11? (yes or no)")

        choice = input()
        if (choice == "yes"):
            userCardOne = 11

    if (userCardTwo == 1):
        print("Do you want to change the value of Ace to 11? (1. yes, 2. no)")

        choice = input()
        choice = input()
        if (choice == "yes"):
            userCardTwo = 11
# DO ONE FOR COMPUTER PICK THE BEST VALUE

    #cards after conversion
    print("Two values: ", userCardOne, "and", userCardTwo)
    print("User total:", userCardOne + userCardTwo)
    print("Computer Cards Value are ", compCardOne, "and", compCardTwo)
    print("Comp total:", compCardOne + compCardTwo)







#main where the code starts
userName = getUserName()
print("Ok", userName, ", Before we get started do you know the rules?"
                      "(1 yes, 2 no)")
choice = input()
choice = int(choice) #convert to a int
if choice == 2:
    rules()
elif (choice != 2 and choice != 1):
    print("Ok,", choice, "wasnt an option...")

playGame(userName)


