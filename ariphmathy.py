import random 
import datetime 

def main():
    start()

def start():
    print('Hello!')
    print("In this game you'll have to answer as many questions as you can in limited time")
    print("Each right answer will give you 1 point")
    begin = input('Do you what to check your arithmathy?(Yes/No) ').lower()
    if begin == 'yes':
        gameBody()
    else:
        print('Ok, bye!')

def gameBody(points = 0):
    # currentMin = int(datetime.datetime.strftime(datetime.datetime.now(), "%M"))
    # currentSec = int(datetime.datetime.strftime(datetime.datetime.now(), "%S"))
    c = 0
    while (c < 11):
        def addition(points):
            randNum1 = random.randint(100, 1001)
            
            randNum2 = random.randint(100, 1001)
            answer = int(input('What is the answer of "'+str(randNum1)+'+'+str(randNum2)+'"? '))
            if answer == randNum1+randNum2:
                points += 1
                print('Right')
            else:
                print('Wrong!')
            return points

        def substraction(points):
            randNum1 = random.randint(100, 1001)
            randNum2 = random.randint(10, 100)
            answer = int(input('What is the answer of "'+str(randNum1)+'-'+str(randNum2)+'"? '))
            if answer == randNum1-randNum2:
                points += 1
                print('Right')
            else:
                print('Wrong!')
            return points

        def multiplication(points):
            randNum1 = random.randint(1, 10)
            randNum2 = random.randint(1, 10)
            answer = int(input('What is the answer of "'+str(randNum1)+'*'+str(randNum2)+'"? '))
            if answer == randNum1*randNum2:
                points += 1
                print('Right')
            else:
                print('Wrong!')
            return points

        def division(points):
            randNum1 = random.randint(10, 100)
            randNum2 = random.randint(2, 100)
            while randNum1 % randNum2 != 0:
                randNum2 = random.randint(2, randNum1//2)
            answer = int(input('What is the answer of "'+str(randNum1)+'/'+str(randNum2)+'"? '))
            if answer == randNum1/randNum2:
                points += 1
                print('Right')
            else:
                print('Wrong!')
            return points
        
        funcs = [addition, substraction, multiplication, division]
        points = random.choice(funcs)(points)
        c+=1
    print('Your time is left!')
    theEnd(points)

def theEnd(points):
    if points <= 0:
        print('You suck(>_<)')
    elif points < 2:
        print('Less than 2 right answers at minute. Are you from kindergarden?')
    elif points <= 5:
        print("You probably didn't study at school")
    elif points <= 8:
        print("Pff.. anyone can do this")
    elif points <= 9:
        print('Not bad)')
    elif points <= 10:
        print('Good job!, now you can easily pass SAT')
    else:
        print('Well, I suspect that you used a calculator:3')

main()