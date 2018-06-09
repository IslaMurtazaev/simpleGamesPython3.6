"""
My little greed game, just for practicing
"""
import random
import time
from threading import Thread
from Greed_player import *

def start_game():
    if ("y" in input("Do you want to play the Greed game? ").lower()):
        print("Great! I'm sure you're gonna like it)\n")
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
    if ("y" in input("Are you familiar with the rules? ").lower()):
        print("Fine, let's start then\n")
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
    print()
    return num_of_players


def create_player_instances(num_of_players):
    names = []
    for i in range(num_of_players):
        while (True):
            name = input("What is the name of player #%d "%(i+1))
            if (name in names):
                print("Please use a different name to make clear distinction")
                continue
            names.append(name)
            break
    print()
    return [Greed_player(name) for name in names]


def play_one_turn(turn, players):
    print("Turn "+ str(turn) +"\n")
    time.sleep(1)
    for player in players:
        print(player.name +" rolling dice..\n")
        time.sleep(1)
        result = player.roll_dice()
        dice = result[0]
        for key in dice.keys():
            if dice[key]:
                print(key +" "+ str(dice[key]))
        print("\n"+ player.name +"'s score: "+ str(result[1])+"\n")
        time.sleep(3)
    print("----------------------------------------------\n")


def is_final_turn(players):
    result = False
    for player in players:
        if (player.get_score() >= 3000):
            print(player.name +" has reached 3000\n")
            time.sleep(1)
            result = True
    return result


def final_turn(players):
    print("Final turn!\n")
    time.sleep(1)
    for player in players:
        print(player.name +" rolling dice..\n")
        time.sleep(1)
        result = player.roll_dice()
        dice = result[0]
        for key in dice.keys():
            if dice[key]:
                print(key +" "+ str(dice[key]))
        print("\n"+ player.name +"'s score: "+ str(result[1]))
        print("In total: "+ str(player.get_score()) +"\n")
        time.sleep(3)


def produce_result(players):
    players_dic = {} # score: name(s)
    for player in players:
        if (player.get_score() in players_dic.keys()):
            players_dic[player.get_score()].append(player.name)
        else:
            players_dic[player.get_score()] = [player.name]

    place = 1
    print("\n\nCongratulations!!\n")
    for score in sorted(players_dic.keys(), reverse=True):
        print(place, ", ".join(players_dic[score]))
        place += 1



def main():
    if(not start_game()): return
    printInstructions()

    players = create_player_instances(prompt_num_of_players())

    turn = 1
    while (not is_final_turn(players)):
        play_one_turn(turn, players)
        turn += 1
        
    final_turn(players)
    produce_result(players)






if __name__ == "__main__":
    main()
