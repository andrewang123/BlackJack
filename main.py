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

def setUpGame(userName):
    cards= [1,2,3,4,5,6,7,8,9,10,11,12,13] # Ace = 1 or 11, J=11, Q=12, K=13
    userCardOne = random.randint(1,13)
    userCardTwo = random.randint(1,13)
    compCardOne = random.randint(1,13)
    compCardTwo = random.randint(1,13)
    # cards before conversion
    print(userName, "your two cards are: ", userCardOne, "and", userCardTwo)
    #print("Computer Cards are ", compCardOne, "and", compCardTwo)
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
        choice = int(input())
        if (choice == 1):
            userCardOne = 11
    if (userCardTwo == 1):
        print("Do you want to change the value of Ace to 11? (1. yes, 2. no)")
        choice = int(input())
        if (choice == "yes"):
            userCardTwo = 11
    #Always choose 11 for the ace value
    if(compCardOne == 1):
        compCardOne = 11
    if(compCardTwo ==1):
        compCardTwo = 11

# DO ONE FOR COMPUTER PICK THE BEST VALUE
    userTotal = userCardOne + userCardTwo
    compTotal = compCardOne + compCardTwo
    #cards after conversion
    print("User total:", userTotal)
    #print("Computer Cards Value are ", compCardOne, "and", compCardTwo)
    #print("Comp total:", compTotal)
    choice = 0
    playGame(choice, userTotal, compTotal)

def playGame(choice, userTotal, compTotal):

    while choice != 2:
        print("1. Hit 2. Stand")
        choice = input();
        choice = int(choice)
        #user chose to hit
        if (choice == 1):
            nextCard = random.randint(1,13)
            print("You pulled", nextCard)
            userTotal += nextCard
            print("Your total is:", userTotal)
            if (userTotal) > 21:
                print("You just went over 21, you lose.")
                print("The computer got", compTotal)
                choice = 2 #exit the while loop
        else:
            print("Your total is:", userTotal)
            print("Computers Total:", compTotal)
            if userTotal > compTotal and userTotal <= 21:
                print("You Win!")
            else:
                print("You Lose!")

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
playAgain = 1
while playAgain == 1:
    setUpGame(userName)
    print("play again? (1. yes, 2.no)")
    playAgain = int(input())

#Make it so if they draw an ace in the middle of the game they can pick again!!!


