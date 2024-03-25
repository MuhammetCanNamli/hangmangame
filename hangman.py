import random
import json

def load_words_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['words']

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '-'
    return display

def main():
    word_list = load_words_from_json('wordlist.json')
    word = choose_word(word_list)
    print(word)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    name = input("What's your name handsome/beauty? : ")
    print("What a nice name. Nice to meet you :)")
    print("Try to guess the word {}.".format(name))

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            prdc = input("You wanna guess the word? (Y/N)")
            if prdc == "Y" or prdc == "y":
                shot = input("C'mon, guess what's the word? : ")
                if shot == word:
                    print("Congrats {}. You guessed the word correctly. The word is {}".format(name, word))
                    break
                else :
                    print("You guessed wrong. Keep trying.")
        else:
            print("Incorrect!")
            incorrect_guesses += 1

        if set(word) <= set(guessed_letters):
            print("Congrats {}. You guessed the word correctly. The word is {}".format(name, word))
            break

        print("Attempts left:", max_attempts - incorrect_guesses)
        if incorrect_guesses >= max_attempts:
            print("Sorry {}! You ran out of attempts! The word was {}".format(name, word))
            break


if __name__ == "__main__":
    main()
