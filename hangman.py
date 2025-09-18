import random

# Load words from words.txt
with open("words.txt") as f:
    words = f.read().splitlines()

# Pick a random word
word = random.choice(words).lower()
word_display = ["_"] * len(word)
guessed_letters = set()
turns = 6

print("Welcome to Hangman!")
print("Guess the word:")
print(" ".join(word_display))

# Game loop
while turns > 0 and "_" in word_display:
    guess = input("\nEnter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter (a-z).")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
        for i, letter in enumerate(word):
            if letter == guess:
                word_display[i] = guess
    else:
        turns -= 1
        print(f"Wrong guess! '{guess}' is not in the word.")
        print(f"Remaining turns: {turns}")

    # Show current progress
    print("Word: " + " ".join(word_display))
    print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

# End game result
if "_" not in word_display:
    print(f"\nCongratulations! You guessed the word: {word}")
else:
    print(f"\nGame Over! The word was: {word}")
