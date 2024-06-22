"""
Author : Nikhil Gaikwad
Date : 19-06-2024
Purpose : Learning Python (project 1)
"""
import random

# introduction to the game and rules of the game
print("\n   Welcome to the game of Snake, Water and Gun")
print('<--------------------------------------------------->\n\n')
print(
    "Rules of the game:\n------------------\nTHE PLAYER WHO REACHES 3 POINTS FIRST WILL WIN THE GAME"
)


# game logic
def game_logic(user_choice, comp_choice):
  print('\n\nLET THE MATCH START!!!!\n')

  if user_choice == 'snake' and comp_choice == 'snake' or user_choice == 'gun' and comp_choice == 'gun' or user_choice == 'water' and comp_choice == 'water':
    return 'tie'

  elif user_choice == 'snake' and comp_choice == 'gun' or user_choice == 'gun' and comp_choice == 'water' or user_choice == 'water' and comp_choice == 'snake':
    return 'Python'

  else:
    return 'User'


# game user and computer points traking and making system
python_points = 0
user_points = 0


def game_points_making(result):
  global python_points
  global user_points
  if result == 'User':
    print("\n------> Yes !!!, You won WON.")
    user_points += 1
  elif result == 'Python':
    print("\n------> Sadly but, PYTHON WON.")
    python_points += 1
  else:
    print("\n------> Wow !! it's an tie. Well done both of you")

  return user_points, python_points


# game loop (main loop)
iteration_loop_2 = 0
iteration_loop_1 = 0
while True:
  iteration_loop_1 += 1
  if iteration_loop_1 >= 2:
    print('--------------------------------------------------------->')

  while True:
    iteration_loop_2 += 1
    comp_choice = ['snake', 'water', 'gun']
    if iteration_loop_2 >= 2:
      print('--------------------------------------------------------->')
    print(f'\nROUND : {iteration_loop_1}')
    print('---------------')
    user_choice = input(
        '\n** --- Enter one of Snake, Water or Gun\n\n-------> ').strip(
        ).lower()
    if user_choice not in comp_choice:
      print(
          "\nWRONG INPUT\nYou can only choose between 'Snake','Water','Gun'\nPLEASE TRY AGAIN"
      )
      continue
    else:
      comp_choice = random.choice(comp_choice)
      print()
      print(f"\n________You had picked {user_choice.upper()}________")
      print(f"\n________ PYTHON had picked {comp_choice.upper()}________")
      break

  points = game_logic(user_choice, comp_choice)
  numbers = game_points_making(points)
  P_1 = numbers[0]
  C_P = numbers[1]

  print(f"\nUsers Score board    : {P_1}")
  print(f"\ncomputer Score board : {C_P}")

  if P_1 == 3:
    print(
        "\n\n-----------> Congrats you won the game <----------------------\n")
    break
  elif C_P == 3:
    print(
        "\n\n-----------> Sadly you lost the game. PYTHON WON <----------------------\n"
    )
    break
