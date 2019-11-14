# Extra Looping Questions
# You’re not required to complete these, these are more of “challenge” questions.

# 1. (Perfect number) A positive integer is called a perfect number if it is equal to the
# sum of all of its positive divisors, excluding itself. For example, 6 is the first perfect number, because
# 6 = 3 + 2 + 1. The next is 28 = 14 + 7 + 4 + 2 + 1.
# Keep a counter of perfect numbers. How many perfect numbers exist before 10,000. Write a program to find these numbers.

def perfect_number():
    '''
    Checks each number in a range if the sum of its divisors are equal to itself
    '''
    # Create a counter accumalator
    counter = 0
    # Prompt user for the max number to check
    max_num = int(input('Enter the amount of number you wish to check for magic numbers: '))
    # for verification create a dictionary to store the numbers
    perfect_nums = {}

    # For each number in range 2 to Max number + 1 // 0 and 1 are unnecessary for checks
    for num2check in range(4, max_num + 1):
        # Get the evenly divisible factors for number
        factors = [num2check // x for x in range(1, num2check) if num2check % x == 0]
        # remove the element == to the num2check
        factors.remove(num2check)
        # add 1 to the list as a factor
        factors.append(1)
        # Check if the sum of factors equals num2check
        if sum(factors) == num2check:
            # increment the counter if true
            counter += 1
            # add the factors and sum to the num2check key
            perfect_nums[num2check] = {'factors': factors, 'sum': sum(factors)}

    print('\nPerfect Numbers:')
    # itererate through the dictionary entries and print the values
    for count, num in enumerate(perfect_nums.keys()):
        # if last item in the dictionary
        if count == len(perfect_nums.keys()) - 1:
            # print the num with the default new line end
            print(f'{num}')
        else:
            # print 'num, ' without the newline to concatenate all of the numbers on one line
            print(f'{num}', end=', ')

    # print the counter
    print(f'There were {counter} perfect numbers within 0-{max_num}.')

# perfect_number()

# 2. (Game: rock, paper, scissors) Programming Exercise 4.17 gives a program that
# plays the rock, paper, scissors game. Revise the program to let the user play continuously until either the user or the
# computer wins more than two times.

from random import randint

def rps():
    # refactor this!!!
    # Optional prompt user for best of # games, otherwise set 3
    BEST_OF = 3
    # set a games needed to win variable to be 1 more than half of the best of # games
    games_2_win = (BEST_OF // 2) + 1
    # set variables to store the # of wins
    player_wins = 0
    opponent_wins = 0
    # optional set player 2/computer opponent
    opponent = 'Computer'
    # build a ditionary containing acceptable choices
    rock_paper_scissors = {
        1 : 'rock',
        2 : 'paper',
        3 : 'scissors'
    }
    # continuously play until wins == games to win
    while player_wins < games_2_win and opponent_wins < games_2_win:
        # display current wins
        print(f'\nCurrent Wins:\tYou: {player_wins}\t{opponent}: {opponent_wins}')
        # get comp choice
        comp_rps = randint(1, 3)
        # prompt user for input
        player_rps = get_player_rps()
        # print the selected choices
        print(f'You played: {rock_paper_scissors[player_rps]}\t{opponent} played: {rock_paper_scissors[comp_rps]}')
        # check for win conditions
        if comp_rps == player_rps:
            # display draw for equal choices
            print("Draw!\nPlay Again!")
            # rock crushes scissors
        elif player_rps == 1 and comp_rps == 3 or comp_rps == 1 and player_rps == 3:
            print('Rock crushes scissors!', end = ' ')
            # if player played rock
            if player_rps == 1:
                print('You Win!')
                player_wins += 1
            # if computer played rock
            elif comp_rps == 1:
                print(f'{opponent} Win!')
                opponent_wins += 1
            # paper covers rock
        elif player_rps == 2 and comp_rps == 1 or comp_rps == 2 and player_rps == 1:
            print('Paper covers rock!', end = ' ')
            # if player played paper
            if player_rps == 2:
                print('You Win!')
                player_wins += 1
            # if computer played paper
            elif comp_rps == 2:
                print(f'{opponent} Win!')
                opponent_wins += 1
            # scissors cut paper
        elif player_rps == 3 and comp_rps == 2 or comp_rps == 3 and player_rps == 2:
            print('Scissors cut paper!', end = ' ')
            # if player played scissors
            if player_rps == 3:
                print('You Win!')
                player_wins += 1
            # if computer played scissors
            elif comp_rps == 3:
                print(f'{opponent} Win!')
                opponent_wins += 1

def get_player_rps():
    # prompts user for input and returns 1, 2, or 3 depending on choice
    # look into refactoring input validation
    try:
        user_input = int(input('Enter your choice (1 = rock, 2 = paper, 3 = scissors):'))
        if user_input not in range(1, 4):
            while user_input not in range(1, 4):
                user_input = input('Invalid Choice: Enter your choice (1/rock, 2/paper, 3/scissors):')
    except ValueError:    
        while user_input not in range(1, 4):
            if user_input.isdigit():
                user_input = int(user_input)
            elif user_input == 'rock':
                user_input = 1
            elif user_input == 'paper':
                user_input = 2
            elif user_input == 'scissors':
                user_input == 3
            else:
                user_input = input('Invalid Choice: Enter your choice (1/rock, 2/paper, 3/scissors):')
    return user_input

# rps()


# 3. (Turtle: draw circles) Write a program that draws 10 circles with centers (0, 0). Like below

import turtle

def draw_circles(p_numCircles):
    # Draws p_numCircles circles around the 0, 0 coordinate with a 5 pixel seperation between circles
    # Optional set turtle shape
    turtle.shape('turtle')
    # optional set turtle speed
    turtle.speed(0)
    # optional set turtle colors (rainbow)
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    # optional set width of the line to be drawn
    turtle.pensize(3)
    # determine the diameter (in pixels) of the circle
    circle = 20
    # turtle draws circles counter clockwise for the bottom of the circle
    for rep in range(p_numCircles):
        # turtle starts at 0,0 coordinate facing east =>
        turtle.penup()
        # set the color based on rep % len colors so that rolors loop if rep is outside the length of colors
        turtle.pencolor(colors[rep % len(colors)])
        # turn the turtle to face south
        turtle.right(90)
        # move to the start position for the circle to be drawn
        turtle.forward(circle)
        # turn the turtle to face east again
        turtle.left(90)
        # start drawing
        turtle.pendown()
        # draw the circle
        turtle.circle(circle)
        # stop drawing
        turtle.penup()
        # return to the 0,0 coordinate
        turtle.goto(0, 0)
        # return turtle to facing east
        turtle.seth(0)
        # increment the circle size
        circle += 5
    
# draw_circles(10)


# 4. (Turtle: display a multiplication table) Write a program that displays a multiplication table
import turtle

def draw_multi_table(p_num):
    # set a constant for the size of the boxes
    SIZE = 40
    # Optional set turtle shape
    turtle.shape('turtle')
    # optional set turtle speed
    turtle.speed(0)
    # optional set turtle colors (rainbow)
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    # optional set width of the line to be drawn
    turtle.pensize(1)
    # Ensure turtle is not drawing
    turtle.penup()
    # goto starting position for the table
    start = lambda y: (-(SIZE * (p_num + 1))/2, ((SIZE * (p_num + 1)) - (2 * SIZE * y))/2)
    # iterate through the number of cells in the table that need to be drawn
    for row in range(p_num + 1):
        # goto the start of the row
        turtle.goto(start(row))
        for col in range(p_num + 1):
            # start drawing
            turtle.pendown()
            # draw the cell
            for r in range(4):
                turtle.forward(SIZE)
                turtle.right(90)
            # stop drawing
            turtle.penup()
            # move to the start of the next cell
            turtle.forward(SIZE)

# call draw the draw table function
# draw_multi_table(12)


# 5. (Turtle: display a lattice) Write a program that displays an 18-by-18 lattice
def draw_lattice(p_num):
    # set a constant for the size of the boxes
    SIZE = 40
    # Optional set turtle shape
    turtle.shape('turtle')
    # optional set turtle speed
    turtle.speed(0)
    # optional set turtle colors (rainbow)
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    # optional set width of the line to be drawn
    turtle.pensize(1)
    # Ensure turtle is not drawing
    turtle.penup()
    # goto starting position for the table
    start = lambda y: (-(SIZE * (p_num))/2, ((SIZE * (p_num)) - (2 * SIZE * y))/2)
    # iterate through the number of cells in the table that need to be drawn
    for row in range(p_num):
        # goto the start of the row
        turtle.goto(start(row))
        for col in range(p_num):
            # start drawing
            turtle.pendown()
            # draw the cell
            for r in range(4):
                turtle.forward(SIZE)
                turtle.right(90)
            # stop drawing
            turtle.penup()
            # move to the start of the next cell
            turtle.forward(SIZE)
# draw_lattice(17)


# 6. (Turtle: plot the sine and cosine functions) Write a program that plots the sine
# function in red and cosine in blue


# 7. (Turtle: chessboard) Write a program to draw a chessboard

def draw_chessboard():
    # set a constant for the size of the boxes
    SIZE = 100
    # Optional set turtle shape
    turtle.shape('turtle')
    # optional set turtle speed
    turtle.speed(0)
    # optional set turtle colors (rainbow)
    colors = ['blanched almond', 'saddle brown']
    # optional set width of the line to be drawn
    turtle.pensize(1)
    # Ensure turtle is not drawing
    turtle.penup()
    # goto starting position for the table
    start = lambda y: (-(SIZE * (8))/2, ((SIZE * (8)) - (2 * SIZE * y))/2)
    # iterate through the number of cells in the table that need to be drawn
    for row in range(8):
        # goto the start of the row
        turtle.goto(start(row))
        for col in range(8):
            if row % 2 == 0:
                turtle.begin_fill()
                # start drawing
                turtle.pendown()
                # draw the cell
                turtle.color(colors[col % 2])
                for r in range(4):
                    turtle.forward(SIZE)
                    turtle.right(90)
                # stop drawing
                turtle.penup()
                turtle.end_fill()
                # move to the start of the next cell
                turtle.forward(SIZE)
            else:
                turtle.begin_fill()
                # start drawing
                turtle.pendown()
                # draw the cell
                turtle.color(colors[(col + 1) % 2])
                for r in range(4):
                    turtle.forward(SIZE)
                    turtle.right(90)
                # stop drawing
                turtle.penup()
                turtle.end_fill()
                # move to the start of the next cell
                turtle.forward(SIZE)

draw_chessboard()