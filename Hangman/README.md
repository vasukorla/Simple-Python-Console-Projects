📝 Hangman Game – Python Project
📌 Description

This is a Python implementation of the classic Hangman word-guessing game. The program randomly selects a word from an external file (words.txt), and the player must guess the letters one at a time. Correct guesses reveal the letters in the word, while wrong guesses reduce the number of turns left. The game ends when the player either successfully guesses the word or runs out of turns.

⚡ Features

Loads words dynamically from a words.txt file (easy to expand).

Displays word progress using underscores (_) for unguessed letters.

Provides feedback after each guess (correct / wrong).

Tracks and displays remaining turns.

Shows all guessed letters to avoid repetition.

Ends with a clear win/lose message.

🎯 What I Learned

File handling in Python (open(), .read().splitlines()).

Using the random module to select words dynamically.

String and list manipulation to update the displayed word.

Input validation and error handling.

Game logic using loops, sets, and conditionals.

🛠 Concepts Used

File I/O (reading from words.txt)

Random module (random.choice())

Strings and lists (tracking guessed letters, updating display)

Loops (while) and conditionals (if-else)

Sets (storing guessed letters)
