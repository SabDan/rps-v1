import random
print('----------------------------')
print('Rock Paper Scissors V-1     ')
print('----------------------------')

player_one = input("What is player one's name? ")
player_two = input("What is player two's name? ")

game_rolls = ['rock', 'paper', 'scissors']


roll_1 = input(f"{player_one}, what is your roll? [rock, paper, or scissors]: ")
roll_1 = roll_1.lower().strip()
if roll_1 not in game_rolls: # if roll is not in the list
    print(f"Sorry {player_one}, {roll_1} is not a valid play!")
roll_2 = input(f"{player_two}, what is your roll? [rock, paper, or scissors?]: ")
roll_2 = roll_2.lower().strip()
if roll_2 not in game_rolls:
    print(f"Sorry {player_two}, {roll_2} is not a valid play!")

print(f"{player_one} rolls {roll_1}")
print(f"{player_two} rolls {roll_2} ")

# Who wins?
winner = None

if roll_1 == roll_2:

    print("Tied play")
elif roll_1 == "rock":
    if roll_2 == 'paper':
        winner = player_two
    elif roll_2 == 'scissors':
        winner = player_one
elif roll_1 == 'paper':
    if roll_2 == 'scissors':
        winner = player_two
    elif roll_2 == 'rock':
        winner = player_one
elif roll_1 == 'scissors':
    if roll_2 == 'rock':
        winner = player_two
    elif roll_2 == 'paper':
        winner = player_one

print("The game is over!")
if winner is None:
    print("It was a tie!")
else:
    print(f"{winner} takes the game!")