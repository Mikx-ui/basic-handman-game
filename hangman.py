"""
corrections to be made
change the format for the acii art 
add more comments for when the word is guessed or not
also create a multiline string displaying the questions and the task for the assignment
also add a while loop that allows you to replay
and add a dictionary of words
"""
import random

hangman_art = """                                                                                         
.::::::::::::::::::::::::::::.                         
=@%************************%@=.                        
=@+                        *@=..                       
=@+                        *@=..                       
=@+                        *@=.                        
=@+                     :#@@@@@#.                      
=@+                    *@*..  .#@*.                    
=@+                   -@#.     .%@:                    
=@+                   :@@..    .@@.                    
=@+                    -@@*-:-*@@:.                    
=@+                    . :+%@%=:                       
=@+                       .*@=                         
=@+                      -@@@@@:.                      
=@+                    -@@+*@=*@@:.                    
=@+                  :@@+..*@=..*@%:.                  
=@+                .@@+.  .*@=   .*@%.                 
=@+                        *@=..                       
=@+                        *@=..                       
=@+                        *@=..                       
=@+                       *@@@+.                       
=@+                     .%@= +@%.                      
=@+                    -@%.   :@@-                     
=@+                  .*@#.     .%@*.                   
=@+                 .@@=         +@%.                  
=@+                :@@:           :@@.                 
=@+                 ...             .                  
=@+                                                    
=@+                                                    
=@+                                                    
=@+                                                    
.#%%%%%%%@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#.                
...............................................                
:----:+=-+-::=---:=.-:--=::...=:-.-+=:++-=--=-::                
...........................  ..... . ...........
"""

with open("dictionary.txt", "r") as file:
    all_words = [line.strip().lower() for line in file if line.strip()]

used_words = []
unused_words = all_words.copy()

def play_hangman(word):
    guessed = ['_'] * len(word)
    attempts = 4
    guessed_letters = []
    hint_used = False

    print("\nWelcome to Hangman!")
    print("Type 'hint' to reveal a letter (once per game).")

    while attempts > 0 and '_' in guessed:
        print(hangman_art)
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

        if len(guess) != 1 or not guess.isalpha():
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
            right_guesses = ["W guessing", "Good shit", "Keep going", "Typeshitt"]
            print(random.choice(right_guesses))
        else:
            attempts -= 1
            wrong_guesses = ["Poor guessing broski", "Try harder", "There's still hope", "Hmm try again"]
            print(random.choice(wrong_guesses))

    if '_' not in guessed:
        print("You guessed it!!", word)
    else:
        print("Damn the word was:", word)

while True:
    if not unused_words:
        print("You've guessed all the words in the dictionary!")
        break

    word = random.choice(unused_words)
    unused_words.remove(word)
    used_words.append(word)
    play_hangman(word)
    print(f"Words remaining: {len(unused_words)}")
    replay = input("\nDo you want to play again? (Y/N): ").upper()
    if replay != 'Y':
        print("Thanks for playing Hangman!")
        break