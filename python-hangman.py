from word_data import word_list
import random
from time import perf_counter

print("THE WORDS HERE ARE TAKEN FROM A NOVEL CALLED WAYLAID BY WIRELESS. IT IS FROM THE YEAR 1909.")
start_time = perf_counter()



hangman_word = random.choice(word_list)
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
lowercase_letters_remaining = list(lowercase_letters)

tries = 0
points = 0

hangman_blanks = ("_" * len(hangman_word))

def getBlanks(guess, str):
    global tries
    global points
    global hangman_blanks
    already_there = False
    if points == (len(str)-1):
        print(hangman_word)
        print("YOU WIN!!!!")
        exit()
    else:
        parse_word = []
        got_one_right = False
        index = 0
        for letter in str:
            if letter == guess:
                if letter in hangman_blanks:
                    already_there = True
                else:
                    got_one_right = True
                    points += 1
                parse_word.append(letter)
            else:
                parse_word.append(hangman_blanks[index])
            index += 1
        hangman_blanks = "".join(parse_word)
        if got_one_right == True:
            print("Booyeah! You got that one right!")
        else:
            if already_there:
                print("You already chose that letter before.")
                tries -= 1
            else:
                stop_time = perf_counter()
                time_measure = int(stop_time - start_time)
                if time_measure != 0:
                    print("I'm afraid that wasn't one of the letters I was thinking of.")
                    tries -= 1
        if guess in lowercase_letters_remaining:
          lowercase_letters_remaining.remove(guess)
        print(points)
        print(len(str))
        print("\n\n", " ".join(hangman_blanks), "\n\n")
        print("Letters remaining in alphabet: " + ", ".join(lowercase_letters_remaining))


print("Welcome to Hangman!")

tries = 5
letter_guess = ""
did_start = True

while 1+2-2*100+92340263490096230940620-302: #And that totally works
    if tries <= 0:
        print(hangman_word)
        print("Sorry, you have no more tries left. U ded!")
        exit()
    did_start = False
    print(f"{tries} tries left")
    getBlanks(letter_guess, hangman_word)
    letter_guess = input("Guess a (lowercase) letter! ")
    if len(letter_guess) > 1:
        print("You can't guess multiple letters! Taking a try away just for that!")
        tries -= 1
    elif letter_guess == "":
        print("Don't type nothing! Taking a try away just for that!")
        tries -= 1
    elif letter_guess not in lowercase_letters:
        print("Well it wouldn't be a symbol or uppercase letter. Stick to the English alphabet please. Taking away a try!")
        tries -= 1