from random import randint

"""
List and Tuple Exercises
​"""
'''
 1. Total Sales
Design a program that asks the user to enter a store’s sales for each day of the week. The
amounts should be stored in a list. Use a loop to calculate the total sales for the week and
display the result.
​'''

def total_sales():
    # Initialize a list to store the inputs
    weekly_sales = []

    # Prompt user for input until there are 7 elements in weekly sales
    while len(weekly_sales) < 7:
        # Prompt user for a days sales
        sales = float(input(f'Enter the sales for day {len(weekly_sales) + 1:}: $'))
        # Prompt again if sales number is negative until a positive number, or 0 is entered
        while sales < 0:
            sales = float(input(f'Invalid input. entry must be positive.\nRe-enter the sales for day {len(weekly_sales) + 1:}'))
        # Append the sales to weekly sales
        weekly_sales.append(sales)

    # initialize a total accumalator
    total = 0

    # Iterate through each element in weekly sales
    for amount in weekly_sales:
        # add the element value to the total accumalator
        total += amount
    
    # Display the total weekly sales
    print(f'\nThe total sales for the week is ${total:,.2f}.')

# total_sales()

'''
 2. Lottery Number Generator
Design a program that generates a seven-digit lottery number. The program should generate seven random numbers, each in the range of 0 through 9, and assign each number to a list element. Then write another loop that displays the contents of the list.
​'''

def lottery_number_generator():
    # Initialize a list to store the inputs
    lottery_numbers = []
    # Initialize an index accumaltor variable for the list insert() method
    ind = 0

    # Prompt user for input until there are 7 elements in lottery numbers
    while ind < 7:
        # insert a random integer into a list element index
        lottery_numbers.insert(ind, randint(0,9))
        # increment the index
        ind += 1

    # reset the index variable to 1 for list print // using this method incase of duplicates elements
    ind = 1

    # iterate through the list elements
    print('\nLottery Numbers are:')
    for element in lottery_numbers:
        # print the element
        print(f'| {ind:>2}:{element:>3} |')
        # increment the ind accumalator
        ind += 1

# lottery_number_generator()

'''
 3. Rainfall Statistics
Design a program that lets the user enter the total rainfall for each of 12 months into a list.
The program should calculate and display the total rainfall for the year, the average monthly
rainfall, and the months with the highest and lowest amounts.
​'''

def rainfall_statistics():
    # Initialize a list to store inputs
    rainfall = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # iterate through each element, month, in the rainfall list
    for month in rainfall:
        # Prompt user for rainfall for the month
        user_input = input(f'Enter the amount of rainfall for {month}: ')
        # Continuously prompt until a positive number is entered
        while float(user_input) < 0:
            user_input = input(f'Invalid input: Only positive number entries are accepted.\nEnter the amount of rainfall for {month}: ')
        # replace the month with the user input
        rainfall[rainfall.index(month)] = float(user_input)

    # Display the total, average monthly, highest, and lowest rainfalls.
    print(f'\nTotal Rainfall:           {sum(rainfall):.2f}')
    print(f'Average Monthly Rainfall: {sum(rainfall)/len(rainfall):.2f}')
    print(f'Highest Rainfall:         {max(rainfall)}')
    print(f'Lowest Rainfall:          {min(rainfall)}')

# rainfall_statistics()

'''
 4. Number Analysis Program
Design a program that asks the user to enter a series of 20 numbers. The program should
store the numbers in a list and then display the following data:
• The lowest number in the list
• The highest number in the list
• The total of the numbers in the list
• The average of the numbers in the list
​'''

def number_analysis():
    # initialize a list to store the user input
    analyze_this = []

    # Continuously Prompt for inputs until the list has 20 elements
    while len(analyze_this) < 20:
        analyze_this.append(float(input('Enter a number for the analysis: ')))
    
    # Display the total, average, lowest, and highest numbers
    print(f'\nLowest number:      {min(analyze_this)}')
    print(f'Highest number:     {max(analyze_this)}')
    print(f'Total sum:          {sum(analyze_this)}')
    print(f'Average of numbers: {sum(analyze_this)/len(analyze_this)}')

# number_analysis()

'''
 6. Driver’s License Exam
The local driver’s license office has asked you to create an application that grades the written portion of the driver’s license exam. The exam has 20 multiple-choice questions. Here
are the correct answers:
1. B 	6. A 	11. B 	16. C
2. D 	7. B 	12. C 	17. C
3. A 	8. A 	13. D 	18. B
4. A 	9. C 	14. A 	19. D
5. C 	10. D 	15. D 	20. A
Your program should store these correct answers in a list. The program should read the
student’s answers for each of the 20 questions from a text file and store the answers in
another list. (Create your own text file to test the application.) After the student’s answers
have been read from the file, the program should display a message indicating whether the
student passed or failed the exam. (A student must correctly answer 15 of the 20 questions
to pass the exam.) It should then display the total number of correctly answered questions,
the total number of incorrectly answered questions, and a list showing the question numbers of the incorrectly answered questions.
​'''

def driver_license_exam():
    # lazy answer list creation
    # set string variable to all of the answers concatenated together
    answers_string = 'BDAACABACDBCDADCCBDA'
    # initialize the answer list
    answers_list = []
    # iterate through each char in the answers string
    for char in answers_string:
        # append each char to the answer list
        answers_list.append(char)
    
    # open the student answer file to be read from // assumed all answers on one line with commas seperating values
    with open('answers.txt', 'r') as answer_file:
        # read the line, strip the trailing newline (\n) and split on the ',' to get one answer per element in a list
        student_answers = answer_file.readline().rstrip('\n').split(',')

    # initialize a correct counter
    num_correct = 0
    # initialize a list to store incorrect answer numbers
    incorrect_list = []
    # iterate over each element in the answers list
    for index in range(len(answers_list)):
        # Check if the student answer == correct answer
        if student_answers[index] == answers_list[index]:
            # increment the correct accumalator
            num_correct += 1
        # else
        else:
            # Append the index + 1 (problem number of incorrect answer) to the incorrect list
            incorrect_list.append(index + 1)
    
    # Display the number of correct answers
    print(f'\n{num_correct}/{len(answers_list)} Correct.')
    # check if incorrect list has any elements
    if len(incorrect_list) > 0:
        print('\nIncorrect Problems:')
        # iterate through each element in the incorrect list
        for problem in incorrect_list:
            # display the problem numbers
            print(f'{problem:>5}.')

# driver_license_exam()

'''
 7. (Largest rows and columns) Write a program that randomly fills in 0s and 1s into
a matrix, prints the matrix, and finds the rows and columns with the most
1s. Here is a sample run of the program:
0011
0011
1101
1010
The largest row index: 2
The largest column index: 2, 3
​'''

def largest_rows_columns():
    # building the matrix
    # initialize the list for the matrix to work in
    matrix = []
    # grab a random integer between 2 and 10, inclusive, to determine the size of the matrix
    SIZE = randint(2,10)
    # iterate through a range up to the rng size variable
    for build_row in range(SIZE):
        # set an empty string to begin building the binary pattern
        m_row = []
        # iterate through a range of the matrix size constant to build the columns entry
        for build_columns in range(SIZE):
            # append a random integer (0, 1) to the row pattern
            m_row.append(randint(0, 1))
        # append the built row to the matrix
        matrix.append(m_row)
    
    # for better formatting add a blank print statement
    print('')
    # Iterate through each row to print the matrix
    for print_row in matrix:
        # Initialize a variable to represent the matrix in string format
        row_str_rep = ''
        # iterate for each element in the row
        for print_char in print_row:
            # add the string value of the element to the string
            row_str_rep += str(print_char)
        # display the rows, one row per line
        print(row_str_rep)

    # reading the matrix
    # initialize a new list to store the results of ones in each row
    calc_rows = []
    # initialize a new list/accumalator to store the results of ones in each column
    calc_columns = [0] * SIZE

    # iterate over each row in the matrix
    for row in matrix:
        # sum the row and append it to calc_rows list
        calc_rows.append(sum(row))
        # Iterate ovet each element in the row to get the column count
        for index in range(len(row)):
            # if element in index == 1 ; do nothing if element != 1
            if row[index] == 1:
                # increment the column counter
                calc_columns[index] += 1

    # assign the max of calcs rows to a variable
    highest_row = max(calc_rows)
    # Check if only one occurance of max value in row
    if calc_rows.count(highest_row) > 1:
        # initial a counter to keep track of removed indexes
        removed_count = 0
        # initialize a list to store multiple indexes
        max_rows = []
        # continuously pull and del indexes until the count of max value == 0
        while calc_rows.count(highest_row) > 0:
            # assign the first index of the max of calc_rows to a variable
            max_val_index = calc_rows.index(highest_row)
            # append the first max value index to the list + the counter of removed indexes
            max_rows.append(str(max_val_index + removed_count))
            # del the index of the first max value
            del(calc_rows[max_val_index])
            # increment counter of removed indexes
            removed_count += 1
        # convert the list to a string for printing
        string_rep_rows = ', '.join(max_rows)
        # print the rows with the greatest value
        print(f'\nlargest row indexes: {string_rep_rows}')
    # if only 1 instance
    else:
        # Display the largest row
        print(f'\nlargest row index: {calc_rows.index(highest_row)}')
    # assign the max of calcs columns to a variable
    highest_column = max(calc_columns)
    # check if only 1 occurance of max value in column
    if calc_columns.count(highest_column) > 1:
        # initial a counter to keep track of removed indexes
        removed_count = 0
        # initialize a list to store multiple indexes
        max_columns = []
        # continuously pull and del indexes until the count of max value == 0
        while calc_columns.count(highest_column) > 0:
            # assign the first index of the max of calc_rows to a variable
            max_val_index = calc_columns.index(highest_column)
            # append the first max value index to the list + the counter of removed indexes
            max_columns.append(str(max_val_index + removed_count))
            # del the index of the first max value
            del(calc_columns[max_val_index])
            # increment counter of removed indexes
            removed_count += 1
        # convert the list to a string for printing
        string_rep_columns = ', '.join(max_columns)
        # print the columns with the greatest value
        print(f'largest column indexes: {string_rep_columns}')
    # if only 1 instance
    else:
        # Display the largest column
        print(f'largest column index: {calc_columns.index(highest_column)}')

# largest_rows_columns()

# ​'''
# 8. (Game: play a tic-tac-toe game) In a game of tic-tac-toe, two players take turns
# marking an available cell in a grid with their respective tokens (either X or
# O). When one player has placed three tokens in a horizontal, vertical, or diagonal
# row on the grid, the game is over and that player has won. A draw (no winner)
# occurs when all the cells in the grid have been filled with tokens and neither player
# has achieved a win. Create a program for playing tic-tac-toe.
# The program prompts two players to alternately enter an X token and an O
# token. Whenever a token is entered, the program redisplays the board on the
# console and determines the status of the game (win, draw, or continue).
# '''
'''
***Needs work***
'''
def tic_tac_toe():
    # build the playspace
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

    # intialize the turn accumalator
    turn = 1
    # initialize a winner found flag
    winner = False
    
    # Continuosly get input until winner is found or board is filled
    while not winner and not turn > 9:
        # display the current game board
        show_board(board)
        # Check if player 1's ('X') or player 2's ('O') turn
        if turn % 2 == 1:
            # get player 1's ('X') move
            play = get_play('X', board)
        else:
            # get player 1's ('O') move
            play = get_play('O', board)
        # add play to board
        board = update_board(board, play)
        # check the updated board for a winner
        winner = check_tictactoe_board(board)
        # increment the turn
        turn += 1

    # check if winner is not False
    if winner != False:
        # display the winner message
        print(f'\n\t{winner} WINS!')
    # else max turn limit exceeded / all possible values filled and all board checks returned false
    else:
        # display tie message
        print('\n\tDRAW!')

def show_board(p_board):
    # Iterates through the board parameter and displays the board
    # (WIP)add screen clear before printing
    # initialize a counter
    placeholder = 1
    # Iterate through each row in the board by index
    for row_ind in range(len(p_board)):
        # intialize a variable to store the row to print
        board_row = ''
        # iterate through each element in the row
        for char_ind in range(len(p_board[row_ind])):
            # check if the this is the center of the edge of the board
            if char_ind == 0 or char_ind == len(p_board[row_ind]) -1:
                # check if char is an X or O
                if p_board[row_ind][char_ind] == 'X' or p_board[row_ind][char_ind] == 'O':
                    # add ' ' char ' ' to the row to print
                    board_row += ' ' + p_board[row_ind][char_ind] + ' '
                else:
                    # add ' ' placeholder ' ' to the row to print
                    board_row += ' ' + str(placeholder) + ' '
            # else
            else:
                if p_board[row_ind][char_ind] == 'X' or p_board[row_ind][char_ind] == 'O':
                    # add '| ' + char + ' |' to the row to print
                    board_row += '| ' + p_board[row_ind][char_ind] + ' |'
                else:
                    # add '| ' + placeholder + ' |' to the row to print
                    board_row += '| ' + str(placeholder) + ' |'
            # increment the counter
            placeholder += 1
        # Display the row
        print(board_row)
        # check if not the last row of the board
        if row_ind != len(p_board[row_ind]) - 1:
            # build a row seperator by the length of the board row
            row_sep = '-' * len(board_row)
            # print a row seperator
            print(row_sep)

def get_play(p_player, p_board):
    # get valid plays for board
    valid_plays = get_valid_plays(p_board)
    # initialize the variable to store the input
    play = -1
    # Display player turn
    print(f'\n\t{p_player} it\'s your turn.')
    # While play is not in valid plays
    while play not in valid_plays:
        # prompt user for input
        try:
            # print('Available Plays:', valid_plays)
            play = int(input('Where do you want to play?: '))
        # if in error, reset play for loop
        except ValueError:
            print('Error: Invalid input.')
            play = -1
    # return the p_player and the play in a list
    return [p_player, play]


def get_valid_plays(p_board):
    # initialize a list to return
    available_plays = []
    # initialize an accumalator to assign to coordinates
    plays = 1
    
    # iterate through the rows of the board
    for row in p_board:
        # iterate through each column in the board row
        for column in row:
            # check if row, column has any plays in it
            if column != 'X' and column != 'O':
                # append the available plays if not played
                available_plays.append(plays)
            # increment the plays accumalator
            plays += 1

    # return the list of available plays
    return available_plays

def update_board(p_board, p_play):
    '''
    takes a board matrix parameter and updates it based on the play parameter
    p_play[0] = 'X' or 'O'
    p_play[1] = value to update
    '''
    # initialize a counter to locate the space to update
    locator = 1
    # iterate through the rows of the board
    for row in range(len(p_board)):
        # iterate over each column of the board row
        for column in range(len(p_board[row])):
            # check if the locator == play
            if locator == p_play[1]:
                # update the board with the play
                p_board[row][column] = p_play[0]
                # return the new board once the board has been updated
                return p_board
            # increment the locator
            locator += 1
    
    # if no change occurs and loop completes
    print('No change to board.')
    # return the board
    return p_board

def check_tictactoe_board(p_board):
    '''
    Takes a 3x3 matrix board in a parameter and checks the columns, rows, and diagonals for 3 consecutive X's or O's
    returns the winner, ('X','O') if any one condition is true, otherwise returns False.
    '''
    # initialize lists containing the possible win conditions
    top_row = [p_board[0][0], p_board[0][1], p_board[0][2]]
    middle_row = [p_board[1][0], p_board[1][1], p_board[1][2]]
    bottom_row = [p_board[2][0], p_board[2][1], p_board[2][2]]
    first_column = [p_board[0][0], p_board[1][0], p_board[2][0]]
    second_column = [p_board[0][1], p_board[1][1], p_board[2][1]]
    third_column = [p_board[0][2], p_board[1][2], p_board[2][2]]
    diag_tlbr = [p_board[0][0], p_board[1][1], p_board[2][2]]
    diag_trbl = [p_board[0][2], p_board[1][1], p_board[2][0]]
    win_conditions = [top_row, middle_row, bottom_row, first_column, second_column, third_column, diag_tlbr, diag_trbl]
    # initialize a flag to return
    winner = False
    # Iterate through each of the win_conditions
    for condition in win_conditions:
        # Check if the first value is an 'X' or an 'O' // removes default values from the possible win conditions
        if condition[0] == 'X' or condition[0] == 'O':
            # Check if all elements are the same
            if condition[0] == condition[1] and condition[1] == condition[2]:
                # set the winner to 'X' or 'O'
                winner = condition[0]
    # return winner
    return winner
    
tic_tac_toe()