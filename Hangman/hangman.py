# Hangman
import random

# Word list
word = random.choice(['python', 'java', 'kotlin'])
guessed = ['_'] * len(word)
tries = 6

print("Welcome to Hangman!")
print("Word to guess:", ' '.join(guessed))

while tries > 0 and '_' in guessed:
    guess = input("\nGuess a letter: ").lower()

    if guess in word:
        if guess in guessed:
            print(f"You already guessed '{guess}' correctly!")
        else:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print(f"✅ Good guess! '{guess}' is in the word.")
    else:
        tries -= 1
        print(f"❌ Wrong guess! '{guess}' is not in the word.")

    print("Word:", ' '.join(guessed))
    print(f"Turns left: {tries}")

# Final result
if '_' not in guessed:
    print("\n🎉 You won! The word was:", word)
else:
    print("\n💀 You lost! The word was:", word)
