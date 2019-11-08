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
from random import randint

def main():
    global profile
    # Main menu to run the game
    menu = {
        1 : {'desc' : 'Play Hangman', 'call' : play_hangman},
        2 : {'desc' : 'Play # of Hangman games', 'call' : play_multi_hangman},
        3 : {'desc' : 'Load Profile', 'call' : load_profile},
        4 : {'desc' : 'View leaderboard', 'call' : view_leaderboard},
        5 : {'desc' : 'Quit'}
    }
    # initialze the user choice to 0
    menu_choice = 0
    # load the profiles databaes
    load_all_profiles()
    # initialize profile with the default 'Guest'
    profile = {'Name' : 'Guest', 'Wins' : 0, 'Games Played' : 0}
    # loop menu until quit option is given
    while menu_choice != 5:
        # display the menu
        print('\t\tMain Menu')
        for key in menu.keys():
            print(' {} : {}'.format(key, menu[key]['desc']))
        # get player's menu choice
        menu_choice = get_menu_choice(menu.keys())
        # call menu choice function unless the menu_choice is 5
        if menu_choice in menu.keys() and menu_choice != 5:
            menu[menu_choice]['call']()

    # if while loop is properly terminated
    # call the update profile function if profile is loaded
    update_all_profiles()
    # print game exit message
    print('Quitting')

def get_menu_choice(p_valid_keys):
    # get user's menu choice
    # Prompt user for a menu choice
    try:
        user_input = int(input('What do you want to do? :'))
        # if user input is not a key in valid keys
        while user_input not in p_valid_keys:
            # Prompt user for valid menu option
            user_input = int(input(f'Invalid option!\nValid options are {p_valid_keys}\nEnter a valid option: '))
    # if user input fails to convert to int
    except ValueError as e:
        # display the error message
        print(f'Invalid option\n{e}')
        # set user input to 0 and return to the menu
        user_input = 0
    # return user input
    return user_input

def play_hangman():
    global hangman_art
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
    computer = get_player()
    try:
        with open('hangedman.dat', 'rb') as infile:
            hangman_art = pickle.load(infile)
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
        # if computer is playing
        if computer:
            # get randomly selected letter
            guessed_letters.append(get_comp_guess(guessed_letters))
        else:
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
        print(f'The word was {hangman_word}')
        # if profile loaded update profile games played
        profile['Games Played'] += 1
    # else if guesses remaining is not 0 and guessed word is equal to chosen word:
    elif guessed_word == hangman_word:
        print(f'\t    {guessed_word}')
        # print the win message
        print('\t\tYou Win!')
        # if profile loaded update profile games played and wins
        profile['Games Played'] += 1
        profile['Wins'] += 1
    else:
        # Error message
        print('Something went wrong. Loop exited without Win/Loss condition met.')

def get_word():
    # Prompt user for a word greater than 3 letters to be used for hangman
    # Or use a randomly select a word from a wordbank
    # (WIP) add valid word in dictionary check
    # Prompt user if they want to use a word from the wordlist
    use_wordlist = input('Would you like to use a randomly generated word? (y/n): ').lower()
    # if yes return the random word
    if use_wordlist == 'y' or use_wordlist == 'yes':
        return get_random_word()
    # Otherwise prompt user for the word to use.
    else:
        user_input = input('Enter a secret word to play: ')
        while len(user_input) < 4:
            user_input = input('Word is too short.\nTry Again: ')
        return user_input.upper()

def display_hangedman(p_guess):
    # Draws the current hangman image based on p_guess
    for line in hangman_art[p_guess]:
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

def get_random_word():
    # Returns a random word selected from the wordlist file
    try: 
        with open('hangman_words.txt', 'r') as wordlist_file:
            wordlist = wordlist_file.readlines()
        rdm_word = wordlist[randint(0, len(wordlist))]
        while len(rdm_word) < 4:
            rdm_word = wordlist[randint(0, len(wordlist))]
        return rdm_word.upper()
    except IOError as e:
        print(e)

def get_comp_guess(p_guessed_letters):
    # generates a randomly selected guess from available letters
    # Populate a list of letters for the computer to choose from
    available_letters = [char for char in string.ascii_uppercase if char not in p_guessed_letters]
    # return a letter from available letters by a random integer index
    return available_letters[randint(0, len(available_letters) - 1)]

def get_player():
    # Returns a boolean value if the computer is playing
    # prompts if user is playing, or computer
    comp = input('Will the computer be playing for you? (y/n): ')
    if comp == 'y' or comp == 'yes':
        return True
    else:
        return False

def load_profile():
    # calls the load all profiles function, prompts user for a name, and loads the associated profile
    global profile
    # prompt user for a name
    user_input = input('Enter the profile name to load: ').title()
    # if the name is in the database
    if user_input in all_profiles.keys():
        #set profile variable = all_profiles[user_input]
        profile = all_profiles[user_input]
    else:
        #Prompt user if they wish to add the name to all_profiles
        option = input(f'Profile not found. Do you wish to create {user_input}\'s profile? (y/n): ')
        # if yes set defaults value to the profile
        if option == 'y' or option == 'yes':
            profile = {'Name' : user_input, 'Wins' : 0, 'Games Played' : 0}
    # if no, return to menu and play as a guest
        

def load_all_profiles():
    # loads a user's profile from a profiles.dat and adds it a global profile dictionary
    global all_profiles
    # Attempt to open the the profiles database
    try:
        with open('profiles.dat', 'rb') as in_file:
            all_profiles = pickle.load(in_file)
    # if the profiles database is missing or corrupt
    except IOError as e:
        # print missing messages
        print(f'\n{e}')
        print('Establishing new database.')
        # create empty dictionary
        all_profiles = {}

def update_all_profiles():
    # updates the all profiles database with users profile and writes it to profiles.dat
    # If profile already in all profiles keys
    if profile['Name'] in all_profiles.keys():
        # update games played and wins record
        all_profiles[profile['Name']]['Wins'] = profile['Wins']
        all_profiles[profile['Name']]['Games Played'] = profile['Games Played']
    else:
        # add the profile to all_profiles
        all_profiles[profile['Name']] = profile
    # write the updated all_profiles to profiles.dat
    with open('profiles.dat', 'wb') as out_file:
        pickle.dump(all_profiles, out_file)

def play_multi_hangman():
    # Prompts user for a number of games to play
    try:
        num_games = int(input('How many games do you wish to play?: '))
        for game in range(num_games):
            # call play hangman
            play_hangman()
            if game < num_games - 1:
                # prompt user if they are finished playing except on the last game
                quit_playing = input('Start the next game? (y/n default=y):')
                if quit_playing == 'n' or quit_playing == 'no':
                    # break the loop and return to the menu
                    break
    except ValueError:
        print('Invalid input! Returning to menu')

def view_leaderboard():
    # iterates through all profiles, sorted by wins, and prints them to a table
    # update all profiles with the current running profile
    update_all_profiles()
    # display the table headers
    print('╔════════════════════╤══════╗')
    print("║       Name         | Wins ║")
    print("╠════════════════════╪══════╣")
    # iterate through all profiles and append them to a list
    all_profiles_list = []
    for name in all_profiles.keys():
        all_profiles_list.append(all_profiles[name])
    # sort the list by profile wins
    all_profiles_list.sort(key=lambda n: n['Wins'], reverse=True)
    # iterate through all profiles list
    for profile in all_profiles_list:
        # display the table entries
        print('║{:^20}|{:^6}║'.format(profile['Name'], profile['Wins']))
    # print the last line of the table
    print('╚════════════════════╧══════╝')

main()