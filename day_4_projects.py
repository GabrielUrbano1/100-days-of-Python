import random as rand

computer_choice = rand.randint(1, 3)


user_input = int(input("type 1 for rock, 2 for paper or 3 for scissors:  "))



rock = 1
scissors = 2
paper = 3

# rock beats scissors
# scissors beats paper
# paper beats rock

if user_input == 1 and computer_choice == 2:
    print(f"you chose Rock the computer chose Scissors You win!")
elif user_input == 1 and computer_choice == 3:
    print(f"you chose Rock the computer chose Paper You lose")
elif user_input == 1 and computer_choice == 1:
    print(f"you chose Rock the computer chose Rock it's a draw!")
elif user_input == 2 and computer_choice == 3:
    print(f"you chose Scissors the computer chose Paper You win!")
elif user_input == 2 and computer_choice == 1:
    print(f"you chose Scissors the computer chose Rock You lose")
elif user_input == 2 and computer_choice == 2:
    print(f"you chose Scissors the computer chose Scissors it's a draw!")
elif user_input == 3 and computer_choice == 1:
    print(f"you chose Paper the computer chose Rock You win!")
elif user_input == 3 and computer_choice == 2:
    print(f"you chose Paper the computer chose Scissors You lose")
elif user_input == 3 and computer_choice == 3:
    print(f"you chose Paper the computer chose Paper it's a draw!")




# rock beats scissors
# scissors beats paper
# paper beats rock


