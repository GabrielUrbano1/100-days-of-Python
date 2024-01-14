print("Welcome to Treasure Island!\nYour mission is to find the treasure.\n*******************************************************************************\n          |                   |                  |                     |\n _________|________________.=""_;=.______________|_____________________|_______\n|                   |  ,-\"_,=\"\"     `\"=.|                  |\n|___________________|__\"=._o`\"-._        `\"=.______________|___________________\n          |                `\"=._o`\"=._      _`\"=._                     |\n _________|_____________________:=._o \"=._.\"_.-=\"'\"=.__________________|_______\n|                   |    __.--\" , ; `\"=._o.\" ,-\"\"\"-._ \".   |\n|___________________|_._\"  ,. .` ` `` ,  `\"-._\"-._   \". '__|___________________\n          |           |o`\"=._` , \"` `; .\". ,  \"-._\"-._; ;              |\n _________|___________| ;`-.o`\"=._; .\" ` '`.\"\` . \"-._ /_______________|_______\n|                   | |o;    `\"-.o`\"=._``  '` \" ,__.--o;   |\n|___________________|_| ;     (#) `-.o `\"=.`_.--\"_o.-; ;___|___________________\n\____/______/______/___|o;._    \"      `\".o|o_.--\"    ;o;____/______/______/____\n/______/______/______/_\"=._o--._        ; | ;        ; ;/______/______/______/_\n____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____\n/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_\n____/______/______/______/______/_____\"=.o|o_.--\"\"___/______/______/______/____\n/______/______/______/______/______/______/______/______/______/______/\n*******************************************************************************")

user_choice = input("You're at a cross road. There is an island in the middle of the lake. Type 'Wait' to wait for a boat or 'Swim' to swim across.")

if user_choice.lower() == "wait":
    user_door = input("You arrive at the island unharmed. there is a house with three doors. one red, one yellow and one blue. which colour do you choose?")
    if user_door.lower() == "red":
        print("Congrats you found the treasure")
    elif user_door.lower() == "yellow":
        print("you step into the room and fall into a trap.\nGAME OVER!")
    elif user_door.lower() == "blue":
        print("You opened a door to the portal of hell and were engulfed by flames.\nGAME OVER!")
elif user_choice.lower() == "swim":
    print("You were attacked by the gaurdian of the lake and drowned\nGAME OVER!")
else:
    print("Please pick a choice")