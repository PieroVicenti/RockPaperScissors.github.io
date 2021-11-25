import random

rock = "🥌"
paper = "📰"
scissors = "✂"
game_img = [rock, paper, scissors]

user_choice = int(input("Press 1 for scissors, press 2 for rock, press 3 for paper"))
print(game_img[user_choice])

computer_choice = random.randint(0, 2)
print("computer chose: ")
print(game_img[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("Please enter a valid number!")
elif user_choice == 0 and computer_choice == 2:
    print("You win my friend!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!!!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice == computer_choice:
    print("it's a draw, let's play again!")
elif user_choice > computer_choice:
    print("You wiiiiiiiiiiin!")