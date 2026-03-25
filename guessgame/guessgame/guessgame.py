secret_word = "secret"
dashes = []
for i in range(len(secret_word)):
    dashes.append("-")
print("".join(dashes))


def get_guess():
    guess = input("Enter a letter: ")
    while len(guess) != 1 or not guess.islower():
        print("Your guess must have exactly one lowercase character!")
        guess = input("Enter a letter: ")
    return guess

def update_dashes(dashes, secret_word, guess):
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            dashes[i] = guess
    return dashes

while True:
    guess = get_guess()
    if guess in secret_word:
        print("That letter is in the secret word! ")
        dashes = update_dashes(dashes, secret_word, guess)
        print("".join(dashes))
    else:
        print("That letter is not in the secret word! ")