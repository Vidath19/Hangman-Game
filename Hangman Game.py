import random

def hangman():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    word = random.choice(words)
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    print("Guess the word by entering one letter at a time.")
    print("You have 6 tries to guess the word correctly.")

    while tries > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        print("\nWord:", guessed_word)
        print("Tries left:", tries)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            tries -= 1

        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word correctly.")
            break

    if tries == 0:
        print("\nGame over! You ran out of tries.")
        print("The word was:", word)

hangman()
