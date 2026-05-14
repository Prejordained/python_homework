def make_hangman(secret_word):
    guesses = []
    def hangman_closure(guess):
        guesses.append(guess)
        display = "".join([a if a in guesses else "_" for a in secret_word])
        print(display)
        return all(a in guesses for a in secret_word)

    return hangman_closure

secret = input("Enter the secret word: ")
game = make_hangman(secret)

while True:
    guess = input("Guess a letter: ")
    won = game(guess)
    if won:
        print("Congratulations! You guessed the word")
        break