# Rock wins against scissors
# Scissors win against paper
# Paper wins against rock
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
gameImages = [rock, paper, scissors]
userChoice = int(input( "What do you choose? type 0 for rock, 1 for paper or 2 for scisssors \n"))

if userChoice >= 3 or userChoice < 0:
    print("You type an invalid number")
else:

    print(gameImages[userChoice])

    computerChoose = random.randint(0, 2)
    print("computer chose: ")
    print(gameImages[computerChoose])

    if userChoice == 0 and computerChoose == 2:
        print("You wins")
    elif computerChoose == 0 and userChoice == 2:
        print("You lose")
    elif computerChoose > userChoice:
        print("You lose")
    elif userChoice > computerChoose:
        print("You wins")
    elif computerChoose == userChoice:
        print("It\'s a draw")
