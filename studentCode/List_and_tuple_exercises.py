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
    
    print(matrix)

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

    print(calc_rows)
    print(calc_columns)
    # Check if only one occurance of max value in row
    if calc_rows.count(max(calc_rows)) > 1:
        # initial a counter to keep track of removed indexes
        removed_count = 0
        # initialize a list to store multiple indexes
        max_rows = []
        # continuously pull and del indexes until the count of max value == 0
        while 
    # Display the largest row
    print(f'{}')

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
