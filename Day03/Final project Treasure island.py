print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to the Tresure Island")
print("your mission is to find the treasure ")
chose1 = input("You\'re at a crossroad were do you want to go? Type left or right ").lower()

if chose1 == "right":
    chose2 = input('You\'ve come to a lake . thar is an island in the middle of the lake'
    'type "wait" to wait for a bot. type "swim" to swim across.').lower()
    if chose2 == "swim":
        chose3 = input("you arrived the island unharmed.  thar is a house with 3 doors. one  red, one yellow, one blue."
              "which colour do you choose?").lower()
        if chose3 == "red":
            print("it is a room full of fire. Game over")
        elif chose3 == "yellow":
            print("you found the tresure you win!")
        elif chose3 == "blue":
            print("you enter a room of beasts. Game over")
        else:
            print("you chose a room that dose\'t exist. Game over")
    else:
        print("you got attacked by angry trout. game over")
else:
    print("You fall into a hall. Game over")
