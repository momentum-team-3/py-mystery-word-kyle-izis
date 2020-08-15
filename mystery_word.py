import random


def get_word():
    # open the file to get its contents
    with open('words.txt') as words:
        wordList = words.readlines()
        # choose one word at random to be The Word that should be guessed
        word = random.choice(wordList)
    return word


def game_difficulty():
    difficulty = ''
    modes = ['easy', 'normal', 'hard']
    while(difficulty not in modes):
        try:
            difficulty = input(
                'Please choose the level of difficulty: Easy, Normal or Hard? ').lower()
            if difficulty == 'easy':
                game_mode = 'easy'
            elif difficulty == 'normal':
                game_mode = 'normal'
            elif difficulty == 'hard':
                game_mode = 'hard'
        except:
            raise ValueError
            continue
    return game_mode


def get_user_guess():
    guess = ''
    while(True):
        try:
            guess = input("Guess ONE letter: ").lower()
            if (len(guess) > 1):
                print('Game only evaluates ONE character at a time')
            elif (len(guess) == 0):
                print('Please enter a valid input of ONE ASCII character')
            elif (len(guess) == 1 and guess.isalpha()):
                print(f"Your guess was: {guess}")
                break
            else:
                print('This program does not accept numbers or special characters.')
        except KeyboardInterrupt:
            break
        except:
            continue
    return guess  # when this function is called, we want to get back what the user guessed


# def guess_in_word(guess=None, word):
#     if guess in word:
#         return True
#     else:
#         return False


def show_blanks_or_letters(guess, word):
    # we will have to alter this:
    # if the letter has been guessed, we should show letters instead of blanks
    output = ''
    for letter in word:
        if letter == guess:
            output += f' {guess} '
        else:
            output += " _ "
    print('\n' + output + + '\n')


def show_blanks(word):
    output = ''
    for letter in word:
        output += ' _ '
    print(f'\n{output}: {len(word)} letters \n')


def play_game():
    # choose a word
    word = get_word()

    # show the user blanks for each letter in the word
    show_blanks(word)
    # have some way for the user to make a guess
    # let's put it in a function!
    guess = get_user_guess()
    show_blanks_or_letters(guess, word)

    # record the guesses
    # possible implementation: set up a list to store the user guess in
    # where and when do we need access to this? Consider where you might store this information and how you will access it and change it
    # guesses = []
    # guesses.append(guess)  # add the guess to the list

    # record the number of tries (wrong guesses) -> maybe do this later

    # compare the guess to the letters in the word.
    # this is definitely a tricky part. Can you think of how you could do this?
    # is the user's guess one of the letters?
    # restated: is the users's guess (letter) in the word?
    # if the letter is in the word
    # show the letter instead of a blank
    # if the letter is not in the word
    # show the blank
    # and subtract one try
    # show the blanks/filled-in-letters to the user again
    # Ask user for a guess again...


if __name__ == "__main__":
    play_game()
    # word = get_word()
    # show_blanks(word)
    # game_difficulty()
    # get_user_guess()
