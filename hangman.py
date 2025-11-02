import random

hangman_stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========="""
]
word_list = ['band', 'rage', 'slave', 'toad', 'wand']
word = random.choice(word_list)
guessed = ['_'] * len(word)
attempts = 4
guessed_letters = []
hint_used = False
print("Welcome to Hangman!")
print("Type 'hint' to reveal a letter (once per game).")
while attempts > 0 and '_' in guessed:
    print(hangman_stages[4 - attempts])
    print("\nWord: " + ' '.join(guessed))
    print(f"Attempts left: {attempts}")
    guess = input("Guess a letter or type 'hint': ").lower()
    if guess == "hint":
        if hint_used:
            print("You've already used your hint.")
            continue
        else:
            for i, letter in enumerate(word):
                if guessed[i] == '_':
                    guessed[i] = letter
                    print(f"Hint used! Revealed letter: {letter}")
                    hint_used = True
                    break
            continue
    if len(guess) != 1:
        print("Please enter a single alphabetic character.")
        continue
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("W guessing")
    else:
        attempts -= 1
        print("Poor guessing broski")
if '_' not in guessed:
    print("You guessed it!!", word)
else:
    print(hangman_stages[4])
    print("Damn the word was:", word)