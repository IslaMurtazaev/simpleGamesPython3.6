# guess my number game
import random
def main():
    game = input("Do you want to play \"Guess my number\" game? Yes/No:").lower()
    if game == "yes":
        print("Guess a number between 1 and 100")
        randomNumber = random.randint(1, 100)
        found = False # flag variable. To see if you guessed it
        while not found:
            try:
                userGuess = int(input("Your guess: "))
                if userGuess == randomNumber:
                    print("You got it!")
                    found = True
                    main()
                else:
                    if userGuess < randomNumber:
                        print("That's not it, my number is greater)")
                    elif userGuess > randomNumber:
                        print("That's not it, my number is less)")
            except:
                print("You can enter only numbers!")
    else:
        print("Ok, see you then)")

if __name__ == "__main__":
    main()