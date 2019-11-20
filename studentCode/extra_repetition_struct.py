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
    for num2check in range(2, max_num + 1):
        # Get the evenly divisible factors for number
        factors = [num2check // x for x in range(2, num2check + 1) if num2check % x == 0]
        # remove the element == to the num2check
        # factors.remove(num2check)
        # add 1 to the list as a factor */ add 1 to the range to get num2check // x = 1 /*
        # factors.append(1)
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
    print(f'There were {counter} perfect numbers within 0 - {max_num}.')

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

import turtle as t

def draw_multi_circles(p_numCircles):
    # Draws p_numCircles circles around the 0, 0 coordinate with a 5 pixel seperation between circles
    # Optional set turtle shape
    t.shape('turtle')
    # optional set turtle speed
    t.speed(0)
    # optional set turtle colors (rainbow)
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    # optional set width of the line to be drawn
    t.pensize(3)
    # determine the diameter (in pixels) of the circle
    circle = 20
    # turtle draws circles counter clockwise for the bottom of the circle
    for rep in range(p_numCircles):
        # turtle starts at 0,0 coordinate facing east =>
        t.penup()
        # set the color based on rep % len colors so that rolors loop if rep is outside the length of colors
        t.pencolor(colors[rep % len(colors)])
        # turn the turtle to face south
        t.right(90)
        # move to the start position for the circle to be drawn
        t.forward(circle)
        # turn the turtle to face east again
        t.left(90)
        # start drawing
        t.pendown()
        # draw the circle
        t.circle(circle)
        # stop drawing
        t.penup()
        # return to the 0,0 coordinate
        t.goto(0, 0)
        # return turtle to facing east
        t.seth(0)
        # increment the circle size
        circle += 5
    
# draw_circles(10)


# 4. (Turtle: display a multiplication table) Write a program that displays a multiplication table

def draw_multi_table(p_num):
    # set a constant for the size of the boxes
    SIZE = 40
    # set a constant font
    FONT = ('Times New Roman', 12, 'normal')
    # Optional set turtle shape
    t.shape('turtle')
    # optional set turtle speed
    t.speed(0)
    # optional set turtle colors (rainbow)
    # colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    # optional set width of the line to be drawn
    t.pensize(1)
    # Ensure turtle is not drawing
    t.penup()
    # goto starting position for the table
    start = lambda y: (-(SIZE * (p_num + 1))/2, ((SIZE * (p_num + 1)) - (2 * SIZE * y))/2)
    # iterate through the number of cells in the table that need to be drawn
    for row in range(p_num + 1):
        # goto the start of the row
        t.goto(start(row))
        for col in range(p_num + 1):
            # start drawing
            t.pendown()
            # draw the cell
            start_shape_coords = (t.xcor(), t.ycor())
            for r in range(4):
                t.forward(SIZE)
                t.right(90)
                # after completeing the 2nd line of the shape, but before starting the 3rd line, r starts at 0
                if r == 1:
                    # get the position of the opposite en of the shape (square)
                    far_shape_coords = (t.xcor(), t.ycor())
            # stop drawing
            t.penup()
            # if row is 0 and col is not 0 write the column numbers header
            if row == 0 and col != 0:
                # calculate the center of the box
                center_coords = [(start_shape_coords[0] + far_shape_coords[0]) / 2, (start_shape_coords[1] + far_shape_coords[1] + FONT[1]) / 2]
                # goto the center of the shape - the FONT size [1]
                t.goto(center_coords[0], center_coords[1] - (FONT[1]))
                # optional set turtle color
                t.color('red')
                # pendown
                t.pendown()
                # write the col number
                t.write(col, align='center', font=FONT)
                # penup
                t.penup()
            # if row is not 0 and col is 0 write the row numbers header
            elif row != 0 and col == 0:
                # calculate the center of the box
                center_coords = [(start_shape_coords[0] + far_shape_coords[0]) / 2, (start_shape_coords[1] + far_shape_coords[1] + FONT[1]) / 2]
                # goto the center of the shape
                t.goto(center_coords[0], center_coords[1] - (FONT[1]))
                # optional set turtle color
                t.color('blue')
                # pendown
                t.pendown()
                # write the col number
                t.write(row, align='center', font=FONT)
                # penup
                t.penup()
            # if row is not 0 and col is not 0 write the product of row * col
            elif row != 0 and col != 0:
                # calculate the center of the box
                center_coords = [(start_shape_coords[0] + far_shape_coords[0]) / 2, (start_shape_coords[1] + far_shape_coords[1] + FONT[1]) / 2]
                # goto the center of the shape
                t.goto(center_coords[0], center_coords[1] - (FONT[1]))
                # optional set turtle color
                t.color('purple')
                # pendown
                t.pendown()
                # write the col number
                t.write(row * col, align='center', font=FONT)
                # penup
                t.penup()
            # reset the turtle color for the next shape to be drawn
            t.color('black')
            # return to the start of the shape
            t.goto(start_shape_coords)
            # move to the start of the next cell
            t.forward(SIZE)

# call draw the draw table function
# draw_multi_table(12)


# 5. (Turtle: display a lattice) Write a program that displays an 18-by-18 lattice
def draw_lattice(p_num):
    # set a constant for the size of the boxes
    SIZE = 40
    # Optional set turtle shape
    t.shape('turtle')
    # optional set turtle speed
    t.speed(0)
    # optional set turtle colors (rainbow)
    # colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    # optional set width of the line to be drawn
    t.pensize(1)
    # Ensure turtle is not drawing
    t.penup()
    # goto starting position for the table
    start = lambda y: (-(SIZE * (p_num))/2, ((SIZE * (p_num)) - (2 * SIZE * y))/2)
    # iterate through the number of cells in the table that need to be drawn
    for row in range(p_num):
        # goto the start of the row
        t.goto(start(row))
        for _ in range(p_num):
            # start drawing
            t.pendown()
            # draw the cell
            for _ in range(4):
                t.forward(SIZE)
                t.right(90)
            # stop drawing
            t.penup()
            # move to the start of the next cell
            t.forward(SIZE)

# def draw_goto_triangle():
# draw_lattice(17)


# 6. (Turtle: plot the sine and cosine functions) Write a program that plots the sine
# function in red and cosine in blue

import math

def draw_sin_cos():
    SIZE = 20
    SCALE = 1
    SAMPLES = 10
    t.shape('turtle')
    t.speed(0)
    draw_graph(SIZE, SCALE)
    draw_sine(SIZE, SCALE, SAMPLES)
    draw_cosine(SIZE, SCALE, SAMPLES)

def draw_graph(size, scale):
    SIZE = size * 10
    t.color('black')
    t.penup()
    # draw the axis
    t.goto(-SIZE, 0)
    t.pendown()
    t.goto(SIZE, 0)
    t.penup()
    t.goto(0, -SIZE)
    t.pendown()
    t.goto(0, SIZE)
    t.penup()
    # goto start point for drawing gradients
    t.goto(-SIZE, 0)
    for x in range(-SIZE, SIZE + 1):
        if x == 0:
            t.goto(0, -SIZE)
            for y in range(-SIZE, SIZE + 1):
                if y % 25 == 0:
                    # t.pendown()
                    # t.seth(180)
                    # t.forward(10)
                    # t.seth(0)
                    # t.forward(20)
                    # t.penup()
                    draw_gradient(10, t.xcor())
                elif y % 5 == 0:
                    # t.pendown()
                    # t.seth(180)
                    # t.forward(5)
                    # t.seth(0)
                    # t.forward(10)
                    # t.penup()
                    draw_gradient(5, t.xcor())
                # t.pendown()
                t.goto(0, y)
                # t.penup()
            t.goto(x, 0)
        elif x % 25 == 0:
            # t.pendown()
            # t.seth(90)
            # t.forward(10)
            # t.seth(270)
            # t.forward(20)
            # t.penup()
            draw_gradient(10, t.xcor())
        elif x % 5 == 0:
            # t.pendown()
            # t.seth(90)
            # t.forward(5)
            # t.seth(270)
            # t.forward(10)
            # t.penup()
            draw_gradient(5, t.xcor())
        # t.pendown()
        t.goto(x, 0)
        # t.penup()

def draw_sine(size, scale, samples):
    SIZE = size * 10
    t.speed(0)
    t.color('red')
    t.penup()
    sine = lambda x: 50*math.sin((x/100)*2*math.pi)
    t.goto(-SIZE, sine(-SIZE))
    t.pendown()
    # x_coords = [x + (y / samples) for x in range(-SIZE, SIZE) for y in range(samples) if x in range(-SIZE, SIZE)]
    # sine_list = [(x, sine(x) * SIZE/2) for x in x_coords]
    # print(sine_list)
    for x in range(-SIZE, SIZE + 1):
        t.goto(x, sine(x))

def draw_cosine(size, scale, samples):
    SIZE = size * 10
    t.speed(0)
    t.color('blue')
    t.penup()
    cosine = lambda x: 50*math.cos((x/100)*2*math.pi)
    t.goto(-SIZE, cosine(-SIZE))
    t.pendown()
    # x_coords = [x + (y / samples) for x in range(-SIZE * scale, SIZE * scale) for y in range(samples) if x in range(-SIZE, SIZE)]
    # cosine_list = [(x, cosine(x) * SIZE/2) for x in x_coords]
    # print(cosine_list)
    for x in range(-SIZE, SIZE + 1):
        t.goto(x, cosine(x))

def draw_gradient(p_length, p_xcoord):
    t.speed(0)
    t.pendown()
    if p_xcoord == 0:
        t.seth(180)
    else:
        t.seth(90)
    t.forward(p_length)
    t.backward(2 * p_length)
    t.penup()

# draw_sin_cos()

# 7. (Turtle: chessboard) Write a program to draw a chessboard

def draw_chessboard():
    # set a constant for the size of the boxes
    SIZE = 100
    # Optional set turtle shape
    t.shape('turtle')
    # optional set turtle speed
    t.speed(0)
    # optional set turtle colors
    t.color('black')
    # define the fill colors
    colors = ['blanched almond', 'saddle brown']
    # optional set width of the line to be drawn
    t.pensize(3)
    # Ensure turtle is not drawing
    t.penup()
    # goto starting position for the table
    start = lambda y: (-(SIZE * (8))/2, ((SIZE * (8)) - (2 * SIZE * y))/2)
    # iterate through the number of cells in the table that need to be drawn
    for row in range(8):
        # goto the start of the row
        t.goto(start(row))
        for col in range(8):
            # alternate color fill between rows and col
            if row % 2 == 0:
                # set the color based on position (returns either the first color, 0 index, or second color, 1 index)
                t.fillcolor(colors[col % 2])
                t.begin_fill()
                # start drawing
                # t.pendown()
                # draw the square
                draw_square(SIZE)
                # for r in range(4):
                #     t.forward(SIZE)
                #     t.right(90)
                t.end_fill()
                # draw the square outline
                # t.color('black')
                # for r in range(4):
                #     t.forward(SIZE)
                #     t.right(90)
                # stop drawing
                # t.penup()
                # move to the start of the next cell
                t.forward(SIZE)
            else:
                # set the color based on position (returns either the first color, 0 index, or second color, 1 index)
                t.fillcolor(colors[(col + 1) % 2])
                t.begin_fill()
                # start drawing
                # t.pendown()
                # draw the square
                draw_square(SIZE)
                # for r in range(4):
                #     t.forward(SIZE)
                #     t.right(90)
                t.end_fill()
                # draw the square outline
                # t.color('black')
                # for r in range(4):
                #     t.forward(SIZE)
                #     t.right(90)
                # stop drawing
                # t.penup()
                # move to the start of the next cell
                t.forward(SIZE)
    t.hideturtle()

def draw_square(p_size):
    for _ in range(4):
        t.pendown()
        t.forward(p_size)
        t.right(90)
        t.penup()

draw_chessboard()