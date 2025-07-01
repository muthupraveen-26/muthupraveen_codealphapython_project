import random

words = ["python", "hangman", "developer", "keyboard", "program"]
word = random.choice(words)
guessed = []
tries = 6

print("Welcome to Hangman Game!")

while tries > 0:
    display_word = ''.join([letter if letter in guessed else '_' for letter in word])
    print("Word:", display_word)

    if '_' not in display_word:
        print("🎉 You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You've already guessed that letter.")
    elif guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        guessed.append(guess)
        tries -= 1
        print(f"Wrong! Tries left: {tries}")

if tries == 0:
    print("😞 You lost. The word was:", word)
