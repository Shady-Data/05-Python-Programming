"""
Task:
    Your task is to implement the Hangman game in Python.
​
Program Specifications:
    1) Output a brief description of the game of hangman and how to play
    2) Ask the user to enter the word or phrase that will be guessed (have a friend enter the phrase 
        for you if you want to be surprised)
    3) Output the appropriate number of dashes and spaces to represent the phrase (make sure it’s clear 
        how many letters are in each word and how many words there are)
    4) Continuously read guesses of a letter from the user and fill in the corresponding blanks if the 
        letter is in the word, otherwise report that the user has made an incorrect guess.
    5) Each turn you will display the phrase as dashes but with any already guessed letters filled in, 
        as well as which letters have been incorrectly guessed so far and how many guesses the user has remaining.
    6) Your program should allow the user to make a total of k=6 guesses.
​
Assignment Notes:
If the letter has already been guessed, output a message to the player and ask for input again.
If the guess entered is not an alphabetic letter, output a message and ask for input again.
​
If the letter is present in the word to be guessed, fill in the blanks appropriately with this particular letter. 
If the complete name has been guessed, the game is over  - player wins the game.  Output a message telling the 
player they have won and quit the game.
​
If the letter/digit is not present in the word to be guessed, give a message to the player indicating that the 
guess is incorrect and remaining number of chances is one less. If remaining number of chances is 0 (zero), 
the game is over  - player loses the game. Output a message that they have lost and what the correct word was.  Quit the game.
​
Bonus:
    You can do one or both of the following:
​
    1) Using a file:
    Instead of asking for user input for the word, make a word bank in a file named hangman_words.txt. 
    Read in the contents of the file and choose a word at random.
​
    2) Forever alone option:
    You enter the word (or it is randomly chosen from the word bank) and have the computer try to guess the letters.
​
    3) Add some more functionality: 
        - Persist user profiles with scores
        - Prompt for which user is playing
        - Ask if the user wants to play a set of games
        - Build a leader board
        
    Have fun, get creative, and demonstrate what you've come up with.
"""
import pickle
import string

def main():
    global hanged_man
    description = '''
    Hangman:
    Take turns guessing letters for either a random selected word or a player's specified word.
    Be careful though. Every time a wrong letter is guessed, a portion of the hanged man is drawn.
    The game ends once the word is guessed or the hanged man completely drawn.
    '''
    # print the description
    print(description)
    # set the counter of remaining guesses
    guesses_remaining = 6
    # get the word to be used for the game
    hangman_word = get_word()
    # create a set of valid letters
    valid_letters = set(hangman_word)
    # initialize an empty string to store the valid letters in position
    guessed_word = '_' * len(hangman_word)
    # update the guessed word with any non letter chars
    guessed_word = update_guessed_word(hangman_word, guessed_word, ' ')
    # initialize an empty list to store guessed letters
    guessed_letters = []
    # load the hanged man image database
    try:
        with open('hangedman.dat', 'rb') as infile:
            hanged_man = pickle.load(infile)
    except IOError:
        print('hangedman.dat is missing exiting program')
        guesses_remaining = 0
        hangman_word = ''
    # play the game until guesses = 0 
    while guesses_remaining > 0 and guessed_word != hangman_word:
        # print the current hangedman
        display_hangedman(guesses_remaining)
        # print the currently guessed letters in the word and '_' if not guessed yet
        display_guessed_word(guessed_word)
        # get the letter guess from the user
        guessed_letters.append(get_letter(guessed_letters))
        # check if latest guess is in valid letters set
        if guessed_letters[-1] in valid_letters:
            # update the word with the letter
            guessed_word = update_guessed_word(hangman_word, guessed_word, guessed_letters[-1])
        else:
            # display letter not in word
            print(f'Oof! No {guessed_letters[-1]}\'s are in the chosen word.')
            # decrement the guesses remaining
            guesses_remaining -= 1
    
    # check if guesses remaining is 0 (game loss)
    print()
    if guesses_remaining == 0:
        # display the hangedman
        display_hangedman(guesses_remaining)
        # display the loss message
        print('\t\tYou Lose.')
        # print the correct word
        print(f'The word was {hangman_word}.')
    # else if guesses remaining is not 0 and guessed word is equal to chosen word:
    elif guessed_word == hangman_word:
        print(f'\t    {guessed_word}')
        # print the win message
        print('\t\tYou Win!')
    else:
        # Error message
        print('Something went wrong. Loop exited without Win/Loss condition met.')

def get_word():
    # Prompt user for a word greater than 3 letters to be used for hangman
    # (WIP) randomly select a word from a wordbank
    # (WIP) add valid word in dictionary check
    user_input = input('Enter a secret word to play: ')
    while len(user_input) < 4:
        user_input = input('Word is too short.\nTry Again: ')
    return user_input.upper()

def display_hangedman(p_guess):
    # Draws the current hangman image based on p_guess
    for line in hanged_man[p_guess]:
        print('\t\t\t', line)

def display_guessed_word(p_guessed_word):
    # display letters that were correctly guessed and '_' if not guessed yet
    print()
    print('\t', end = '')
    for char in p_guessed_word:
        print(f' {char} ', end='')
    print()

def get_letter(p_guessed_letters):
    # Prompts player for a letter, check if the letter has already been guess, and returns a newly guessed letter
    # Display the already guessed letters
    print('Letters Guessed: ', end ='')
    for count, char in enumerate(p_guessed_letters):
        if count == len(p_guessed_letters) - 1:
            print(f'{char}')
        else:
            print(f'{char}', end = ', ')
    # generate a list of available letters
    available_letters = [char for char in string.ascii_uppercase if char not in p_guessed_letters]
    # prompt user for a letter
    user_input = input('Guess a letter: ').upper()
    while user_input in p_guessed_letters or user_input not in string.ascii_uppercase:
        print(available_letters)
        user_input = input('Invalid guess:\nPlease enter an unguessed letter:').upper()
    return user_input

def update_guessed_word(p_secret_word, p_guessed_word, p_letter):
    # updates guessed word letters by letter if the char in p_secret_word == p_letter
    # returns the update guessed word string
    # create a list of chars from p_guessed_word
    word_letter_list = [char for char in p_guessed_word]
    # enumerate through the p_secret_word chars
    for ind, char in enumerate(p_secret_word):
        # if char == p_letter
        if char == p_letter:
            # set the index of the char in p_guessed_word list to p_letter:
            word_letter_list[ind] = p_letter
        # compensate for any non letter possibilities
        elif char not in string.ascii_uppercase:
            word_letter_list[ind] = char
    # return a string built from the updated p_guessed_word list
    return ''.join(word_letter_list)


main()