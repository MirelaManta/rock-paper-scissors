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

graphic_hand = [rock, paper, scissors]

print("Let's play 'Rock, paper, scissors'!")
your_choice = int(input("What is your play? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n" ))
if your_choice >= 3 or your_choice < 0:
    print("Invalid number, you lose!")
else:
    print(graphic_hand[your_choice])

    robo_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(graphic_hand[robo_choice])

    if your_choice == 0 and robo_choice == 2:
        print("You win!")
    elif robo_choice == 0 and your_choice == 2:
        print("You lose!")    
    elif your_choice < robo_choice:
        print("You lose!")
    elif robo_choice < your_choice:
        print("You win!")     
    elif your_choice == robo_choice:
        print("It's a draw.")
  
