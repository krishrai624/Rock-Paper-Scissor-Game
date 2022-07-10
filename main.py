# we have three people in that three person two are AI and one is real. we have to choose one in Rock, Paper and Scissors.
# And rock win with scissors, paper win with rock and scissors win with paper.
# Display who win but you have ot play 10 times to choose winner. And also display who wins how many times.

import random as rd

print("Please enter the words given Rock as r, Paper as p and Scissor as s\n")

given = ["r", "p", "s"]
play = 0
player_point = 0
com_point = 0
game_over = 10
draw_point = 0

while play < 9:
    player = input("Player 1 choose between r, p and s to win: ", )
    play = play + 1
    com = rd.choice(given)
    print("Computer 1 choose between r, p and s to win: ", com)

    if player == com:
        print("Draw, No one receive point.\n")
        draw_point = draw_point + 1
        print("Draw point is ",draw_point)
    elif player == "r" and com == "p":
        com_point = com_point +1
        print(f"Player choose is {player} and computer choose {com}")
        print("Computer wins\n")
    elif player == "r" and com == "s":
        player_point = player_point +1
        print(f"Player choose is {player} and computer choose {com}")
        print("Player wins\n")
    elif player == "p" and com == "s":
        com_point = com_point +1
        print(f"Player choose is {player} and computer choose {com}")
        print("Computer wins\n")
    elif player == "p" and com == "r":
        player_point = player_point +1
        print(f"Player choose is {player} and computer choose {com}")
        print("Player wins\n")
    elif player == "s" and com == "r":
        com_point = com_point +1
        print(f"Player choose is {player} and computer choose {com}")
        print("Computer wins\n")
    elif player == "s" and com == "p":
        player_point = player_point +1
        print(f"Player choose is {player} and computer choose {com}")
        print("Player wins\n")
    else:
        print("You enter invalid value.\n")
    print(f"Player point is {player_point} and Computer point is {com_point}\n")

    game_over = game_over -1
    print("Play left", game_over)
print(f"Player point is {player_point}\nComputer point is {com_point}\nDraw point is {draw_point}\n")
if player_point == com_point:
    print("Draw, both gain equal point")
elif player_point > com_point:
    print("Player win.")
else:
    print("Computer win.")
