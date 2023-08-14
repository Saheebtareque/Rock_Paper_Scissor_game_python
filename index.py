import sys
import random
from enum import Enum
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

print("")
playerchoice = input("Enter..\n 1.For Rock \n 2.For Paper \n 3.For Scissor \n")
player = int(playerchoice)
if player < 1 or player > 3:
    sys.exit("Please You must enter between 1-3:")
print("Player choice is: " + str(RPS(player)).replace("RPS.","") + ".")
computerchoice = random.choice("123")
computer = int(computerchoice)
print("Computer choice is:", str(RPS(computer)).replace("RPS.","")+ ".")

if player == 1 and computer == 3:
    print("You win")
elif player == 2 and computer == 1:
    print("You win")
elif player == 3 and computer == 2:
    print("You win")
elif player == computer:
    print("It is a draw game")
else:
    print("You lost the game")
