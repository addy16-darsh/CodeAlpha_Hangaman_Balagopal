import random

def choose_word():
    # List of words for the game
    words = ["python", "hangman", "programming", "developer", "engineer", "electronics", "communication"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts = 6  # Number of wrong guesses allowed

    while attempts > 0:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        print(f"Remaining attempts: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        if all(letter in guessed_letters for letter in word_to_guess):
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break
    else:
        print("\nGame Over! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
