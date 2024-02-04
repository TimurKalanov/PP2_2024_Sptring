import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret = random.randint(1,20)
    guesses_taken = 0
    while True:
        print("Take a guess.")
        gues = int(input())
        guesses_taken += 1
        if gues < secret:
            print ("Your guess is too low.")
        elif gues > secret:
            print ("Your guess is too high")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
guess_the_number()