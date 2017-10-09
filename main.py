import sys #user input

#gets the users name
def getUserName():
    name = input('What is your name? ')
    print("Hello", name)
    choice = input("Would you like to play Black Jack? (1 yes, 2 no)")
    choice = int(choice)
    if choice == 1 :
        print("Ok cool, let us get started")
    elif choice == 2 :
        print("Ok... maybe some other time...")
        exit()
    return name


userName = getUserName()
print("Horray you made it")
