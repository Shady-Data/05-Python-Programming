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

    # print the counter
    print(f'There were {counter} perfect numbers within 0-{max_num}.')

perfect_number()

# 2. (Game: rock, paper, scissors) Programming Exercise 4.17 gives a program that
# plays the rock, paper, scissors game. Revise the program to let the user play continuously until either the user or the
# computer wins more than two times.



# 3. (Turtle: draw circles) Write a program that draws 10 circles with centers (0, 0). Like below



# 4. (Turtle: display a multiplication table) Write a program that displays a multiplication table



# 5. (Turtle: display a lattice) Write a program that displays an 18-by-18 lattice



# 6. (Turtle: plot the sine and cosine functions) Write a program that plots the sine
# function in red and cosine in blue


# 7. (Turtle: chessboard) Write a program to draw a chessboard

