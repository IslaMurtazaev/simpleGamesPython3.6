"""
My little greed game, just for practicing
"""
import random
from Greed_player import *

def start_game():
    if ("yes" in input("Do you want to play the Greed game? ").lower()):
        print("Great! I'm sure you're gonna like it)\n\n")
        return True
    else:
        print("Ok( I guess it's goodbye then..")
        return False


def loadInstructions():
    try:
        game_rules = open("python_games/GREEDS_RULES.txt", "r")
        rules = game_rules.read()
        game_rules.close()
    except:
        print("Could not load the \"GREEDS_RULES.txt\" file\n")
        return
    return rules


def printInstructions():
    if ("yes" in input("Are you familiar with the rules? ").lower()):
        print("Fine, let's start then\n\n")
    else:
        print("Ok, here you are\n")
        print(loadInstructions())


def prompt_num_of_players():
    num_of_players = None
    while (num_of_players.__class__ != int or num_of_players < 2):
        try:
            num_of_players = int(input("How many players are going to play? "))
        except:
            print("Number of players must be at least 2")
    print("\n")
    return num_of_players


def create_player_instances(num_of_players):
    players = []
    for i in range(num_of_players):
        players.append(Greed_player(input("What is the name of player #%d "%(i+1))))
    print("\n")
    return players


def play_one_turn():
    pass
    


def main():
    # result = Greed_player("test").roll_dice()
    # dice = result[0]
    # for key in sorted(dice.keys()):
    #     if dice[key]:
    #         print(key +" "+ str(dice[key]))
    # print("the score "+ str(result[1]))
    if(not start_game()): return
    printInstructions()
    players = create_player_instances(prompt_num_of_players())
    for player in players:
        print(player.get_score())






if __name__ == "__main__":
    main()
