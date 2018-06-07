import random

class Greed_player(object):
    def __init__(self, name="unknown"):
        self.name = name
        self.__totalScore = 0


    def get_score(self):
        return self.__totalScore
    
    def set_score(self, new_score):
        assert(new_score >= 0)
        self.__totalScore = new_score

    def count_score(self, dice):
        score = 0
        for key in dice.keys():
            if dice[key] >= 3:
                if (key == "ones"): score += 1000
                elif (key == "sixes"): score += 600
                elif (key == "fives"): score += 500
                elif (key == "fours"): score += 400
                elif (key == "threes"): score += 300
                else: score += 200
                dice[key] -= 3
            if (key == "ones"): score += dice[key] * 100
            elif (key == "fives"): score += dice[key] * 50
        return score
        
    def roll_dice(self):
        dice = {"ones": 0, "twos": 0, "threes": 0, "fours": 0, "fives": 0, "sixes": 0}
        for d in range(6):
            d = random.randint(1,6)
            if (d == 1):
                dice["ones"] += 1
            elif (d == 2):
                dice["twos"] += 1
            elif (d == 3):
                dice["threes"] += 1
            elif (d == 4):
                dice["fours"] += 1
            elif (d == 5):
                dice["fives"] += 1
            else:
                dice["sixes"] += 1

        score = self.count_score(dice.copy())

        self.set_score(self.get_score() + score)
        return (dice, score)

