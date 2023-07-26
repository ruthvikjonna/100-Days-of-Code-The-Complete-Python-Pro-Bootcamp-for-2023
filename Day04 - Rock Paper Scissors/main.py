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

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("\nYou chose:")

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)

print("\nComputer chose:")

computer = random.randint(0, 2)

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)

if user == computer:
    print("\nYou tie!")
elif (user == 0 and computer == 1) or (user == 1 and computer == 2) or (user == 2 and computer == 0):
    print("\nYou lose!")
elif (user == 1 and computer == 0) or (user == 2 and computer == 1) or (user == 0 and computer == 2):
    print("\nYou win!")

print("\n-\n")
