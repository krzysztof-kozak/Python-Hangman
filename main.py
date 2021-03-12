from random import choice
from replit import clear
from hangman_art import logo, stages
from hangman_words import word_list

lives = 6
display = []
chosen_word = choice(word_list)

for _ in chosen_word:
    display += "_"

print(logo, "\n")
print(stages[lives])
print(display)

while chosen_word != "".join(display) and lives:
    guess = input("\nGuess a letter:\n").lower()
    clear()

    if guess in display:
        print(f"You already guessed {guess}...")

    else:
      for index, letter in enumerate(chosen_word):
          if guess == letter:
              display[index] = letter

      if guess in chosen_word and len(guess) > 0:
          print(f"You guessed {guess} and you guessed right!")

      else:
        if len(guess.strip()) < 1:
          print("You tried an empty space...\nNot so great idea...\nHave a -1 life!")
        else:
            print(f"You guessed {guess} but you guessed wrong...")
        lives -= 1

    print("\n", logo)
    print(stages[lives])
    print(display)

if not lives:
    print(f"You lose. The word was {chosen_word}")

else:
    print(f"\nYou won! The word was {chosen_word}. GG.")
