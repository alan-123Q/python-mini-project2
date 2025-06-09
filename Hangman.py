import random

def choose_word():
    words = ["singapore", "china", "canada", "russia", "italy"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6
    print("Welcome to Hangman! \nClue: Its a country")
    print(display_word(word, guessed_letters))

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            tries -= 1
            print(f"Incorrect guess. You have {tries} tries remaining.")
        
        print(display_word(word, guessed_letters))

        if "_" not in display_word(word, guessed_letters):
           print("Congratulations! You guessed the word.")
           return
        
    print(f"Game over! The word was: {word}")

hangman()