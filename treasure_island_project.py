from winreg import REG_DWORD

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('While you\'re travelling, you end up at a cross road. '
                'Where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "left":
#instead of the .lower(), we can also write: if choice1 == "left" or choice1 == "Left" or choice1 == "LEFT":
    choice2 = input('You\'ve come into a lake. '
                    'There is an island in the middle of the lake. ' 
                    'You may swim into the lake or wait for a boat. '
                    'Type "wait" to wait. '
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":


        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. "
                        "One red, one yellow, and one blue. Which colour do you choose?\n").lower()
        if choice3 == "yellow":
            print("You proceed to a dark room.")

            choice4 = input('The dark room leads to a pathway blocked by a swinging razor-edged pendulum. '
                            'You can try cross the pathway. '
                            'Alternatively, you can wait for the pendulum to withdraw to the ceiling. '
                            'Type "cross" for option 1. Type "wait" for option 2.\n').lower()

            if choice4 == "wait":
                print("You avoided the pendulum and reached the deepest room.")

                choice5 = input('You are now inside another room. '
                                'Suddenly, the walls become red-hot and start to move inwards. '
                                'Do you run as quickly as you can until the other end of the room? '
                                'Or do you go back? '
                                'Type "Run" for option 1. Type "Go back" for option 2.\n').lower()

                if choice5 == "run":
                    print("You finally discovered the treasure and another way out. You win!")
                else:
                    print("The door behind you is locked. You are smashed by the closing walls... Game over.")

            else:
                print("The razor-sharp pendulum slices into you.")

        elif choice3 == "red":
            print("You are burned by fire... Game over.")
        elif choice3 == "blue":
            print("You enter a room full of beasts... Game over.")

        else:
            print("Game over.")
    else:
        print("You are chased and eaten by crocodiles... Game over.")
else:
    print("You fell into a pit of spikes... Game over.")



