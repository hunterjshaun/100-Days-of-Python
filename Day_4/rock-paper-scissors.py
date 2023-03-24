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

#Write your code below this line 👇

hand_choice = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
player_choice = hand_choice[player]
print(player_choice)
print("Computer chose:")
computer_choice = random.choice(hand_choice)
print(computer_choice)
if player_choice == computer_choice:
    print("tie")
elif player_choice == rock and computer_choice == paper:
    print("lose")
elif player_choice == paper and computer_choice == scissors:
    print("lose")
else:
    print("win")


