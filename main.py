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
user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors '))
computer_moves =[rock,paper,scissors]
random_move = random.randint(0,len(computer_moves) - 1 )
random_computer_move = computer_moves[random_move]
if user_input == 0:
  print(rock)
  print(f'computer chose: {random_computer_move}')
  if random_move == user_input:
    print('Draw')
  elif random_move == 1:
    print("You win")
  else:
    print("You lose")
if user_input == 1:
  print(paper)
  print(f'computer chose: {random_computer_move}')
  if random_move == user_input:
    print('Draw')
  elif random_move == 0:
    print("You win")
  else:
    print("You lose")
if user_input == 2:
  print(scissors)
  print(f'computer chose:/n {random_computer_move}')
  if random_move == user_input:
    print('Draw')
  elif random_move == 1:
    print("You win")
  else:
    print("You lose")

