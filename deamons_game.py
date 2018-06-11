import time
global gold
global deamons
deamons = 0
gold = 0

def start():
    print ("Hello my friend and welcome to deamon mine!")
    name = input("What's your name?")
    print ("Nice to meet you " + name + "!")
    print ("The objective of this game is to collect deamons and sell them for gold")
    choice = input("Do you want to play? Yes/No ").lower()
    if choice == "yes":
        begin()
    elif choice == "no":
        print("Ok, bye...")
def begin():
    global deamons
    global gold
    print("Let's get started!")
    if gold > 999:
        print("You won the game!")
        play = input("Do you want to play again?")
        if play == "Yes":
            begin()
        elif play == "No":
            print("Congrats again!")
    collect = input("Do you want to collect a deamon? Yes/No ")
    if collect == "Yes":
        time.sleep(1)
        print("You've got a deamon")
        deamons = deamons + 1 
        print("You currently have " ,deamons, " deamons")
        begin()
    elif collect == "No":
       sell = input("Do you want to sell your deamons? Yes/No ")
       if sell == "Yes":
           #global gold
           #global deamons
           print("You currently have " ,deamons, " deamons")
           print("You've sold all your deamons")
           gold = deamons*100
           deamons = 0
           print("You have now " + str(gold) + " gold")
           begin()
start()