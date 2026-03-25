number = 3
guesses_left = 5


while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess != number and guesses_left > 0:
        print("Wrong guess. Try again.")
        guesses_left = guesses_left - 1
        print("you have", guesses_left, "guesses left.")
    elif guesses_left == 1:
        print("Sorry, you've run out of guesses. The correct number was", number)
        break