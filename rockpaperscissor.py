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

images=[rock,paper,scissors]
user_choice=int(input("Enter your choice. Type 0 for Rock, 1 for paper, 2 for scissors\n"))
if 0 <= user_choice <= 2:
    print("You chose: ")
    print(images[user_choice])
comp_choice=random.randint(0,2)
print("Computer chose: ")
print(images[comp_choice])
if user_choice>2 or user_choice<0:
    print("Invalid choice")
elif user_choice==0 and comp_choice==2:
    print("You win")
elif user_choice==2 and comp_choice==0:
    print("You lose")
elif user_choice>comp_choice:
    print("You win")
elif comp_choice>user_choice:
    print("You lose")
elif user_choice==comp_choice:
    print("Draw")