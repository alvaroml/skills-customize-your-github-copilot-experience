# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game to practice string manipulation, loops, conditionals, user input, and random selection.
Build a command-line Hangman game to practice string manipulation, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Implement the Hangman game

#### Description
Create a playable Hangman program (you can start from `starter-code.py`) that randomly selects a secret word and allows a player to guess letters until they either reveal the word or exhaust their allowed incorrect guesses.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Display the current word progress using underscores and revealed letters (e.g., _ a _ _ m a n).
- Accept single-letter guesses from the user, ignore repeated guesses, and validate input.
- Track and display the number of incorrect guesses remaining.
- End with a clear win or lose message; reveal the secret word on loss.
- Optionally display the list of letters already guessed.

#### Example session
```text
Secret word: _ _ _ _ _ _
Guesses left: 6
Enter a letter: a
Good guess: _ a _ _ _ _
Guesses left: 6
Enter a letter: z
Wrong guess: _ a _ _ _ _
Guesses left: 5
```
