import random
from hangman_words import word_list

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
lives = 6

print(logo)


display = []
for i in range(len(chosen_word)):
    display.append("_")

print()
print(f"{' '.join(display)}")
print()

already_guessed = []
while "_" in display:
    guess = input("Guess a letter: ").lower()
    
    if guess not in already_guessed:
        already_guessed.append(guess)
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed the letter {guess}, that's not in the word. You have {lives} lives remaining.")
    else:
        print(f"You've already guessed the letter {guess}.")

    index = 0
    for i in chosen_word:
        if i == guess:
            display[index] = i
        index += 1

    print(f"{' '.join(display)}")
    print(stages[lives])
    
    if lives == 0:
        print(f"{' '.join(chosen_word)}")
        print()
        print("You lose.")
        break
    
if lives > 0:
    print("You win!")
