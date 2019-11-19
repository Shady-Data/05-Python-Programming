# Towers of Hanoi
# Rules:
    # Only one disk may be moved at a time
    # A disk cannot be placed on a smaller disk
    # All disks must be stored on a peg except while being moved
    # You must move all disks from the first peg to the third peg

# This program simulates the Towers of Hanoi game
def main():
    # Set up some initial values
    # num_disks = 3
    num_disks = 9
    from_peg = 1
    to_peg = 3
    temp_peg = 2

    # Play the game
    move_disks(num_disks, from_peg, to_peg, temp_peg)
    print('All the disks are moved')

# The move_disks function displays a disk move in
# the Towers of Hanoi game
# the parameters are:
#   num:        the number of disks to move
#   from_peg:   the peg to move from
#   to_peg:     the peg to move to
#   temp_peg:   the temporary peg
def move_disks(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_disks(num - 1, from_peg, temp_peg, to_peg)
        print('Move a disc from peg', from_peg, 'to peg', to_peg)
        move_disks(num - 1, temp_peg, to_peg, from_peg)

# Call the main function
main()