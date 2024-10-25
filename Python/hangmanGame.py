import random

def hangman_game():
    words = ['python', 'hangman', 'programming', 'development']
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    while attempts > 0:
        current_state = ''.join(letter if letter in guessed_letters else '_' for letter in word_to_guess)
        print(f"\nCurrent word: {current_state}")
        print(f"Attempts remaining: {attempts}")

        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
    else:
        print(f"Game over! The word was: {word_to_guess}")

# Start the game
hangman_game()
