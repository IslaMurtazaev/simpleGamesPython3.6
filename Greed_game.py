"""
My little greed game, just for practicing
"""
import random
from Greed_player import *

def start_game():
    if ("yes" in input("Do you want to play the Greed game? ").lower()):
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
    if ("yes" in input("Are you familiar with the rules? ").lower()):
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
    players = []
    for i in range(num_of_players):
        players.append(Greed_player(input("What is the name of player #%d "%(i+1))))
    print()
    return players


def play_one_turn(turn, players):
    print("The turn number "+ str(turn) +"\n")
    for player in players:
        print(player.name +" rolling dice")
        result = player.roll_dice()
        dice = result[0]
        for key in dice.keys():
            if dice[key]:
                print(key +" "+ str(dice[key]))
        print(player.name +"'s score: "+ str(result[1]) +"\n")


def is_final_turn(players):
    result = False
    for player in players:
        if (player.get_score() >= 3000):
            print(player.name +" has reached 3000\n")
            result = True
    return result


def final_turn(players):
    print("Final turn!\n")
    for player in players:
        print(player.name +" rolling dice")
        result = player.roll_dice()
        dice = result[0]
        for key in dice.keys():
            if dice[key]:
                print(key +" "+ str(dice[key]))
        print(player.name +"'s score: "+ str(result[1]))
        print("In total: "+ str(player.get_score()) +"\n")


def determine_winner(players):
    max_score = max([pl.get_score() for pl in players])
    winners = [pl for pl in players if pl.get_score() == max_score]
    if (len(winners)) > 1:
        print("We have more than "+ str(len(winners)) +" winners!")
        for winner in winners:
            print(winner.name)
    else:
        print("We have a winner!")
        print(winners[0].name)


def main():
    if(not start_game()): return
    printInstructions()

    players = create_player_instances(prompt_num_of_players())

    turn = 1
    while (not is_final_turn(players)):
        play_one_turn(turn, players)
        turn += 1
        
    final_turn(players)
    determine_winner(players)






if __name__ == "__main__":
    main()
