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

user_choice = str(input("If you want play, make a choice between Rock, Scissors, Paper\n").lower())
#the list of "pictures" 
paints_arr = [rock, paper, scissors]
#list of user's decisions
arr = ['rock', 'paper', 'scissors']
#random choice of the computer with the random method
computer_choice = random.randint(0, len(arr) - 1)

if user_choice == arr[computer_choice]:
    print(f"You and your opponent made the same choice, nobody wins, please play again.")
else:
    if arr[computer_choice] == 'rock' and user_choice == 'paper':
        print(f"You Win with paper!\n{paper}")
        print(f"Computer lose with {arr[computer_choice]}!\n{paints_arr[0]}")
    elif arr[computer_choice] == 'paper' and user_choice == 'scissors':
        print(f"You Win with scissors!\n{scissors}")
        print(f"Computer lose with {arr[computer_choice]}\n{paints_arr[1]}")
    elif arr[computer_choice] == 'scissors' and user_choice == 'rock':
        print(f"You Win with rock!\n{rock}")
        print(f"Computer lose with {arr[computer_choice]}!\n{paints_arr[2]}")
    else: 
        print(f"Computer win with {arr[computer_choice]}! You lose.\n{paints_arr[computer_choice]}")







