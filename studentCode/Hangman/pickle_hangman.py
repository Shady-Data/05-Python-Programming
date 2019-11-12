'''
Write a dictionary containing hangman images and stores it in a serialized file called hangedman.dat
'''
import pickle

def main():
    # populate a dictionary with the ascii art to be drawn with a key of remaining guesses
    hangedman = {
        6 :[
          '  +---+  ',
          '  |   |  ',
          '      |  ',
          '      |  ',
          '      |  ',
          '      |  ',
          '========='
        ],
        5 :[
          '  +---+  ',
          '  |   |  ',
          '  O   |  ',
          '      |  ',
          '      |  ',
          '      |  ',
          '========='
        ],
        4 :[
          '  +---+  ',
          '  |   |  ',
          '  O   |  ',
          '  |   |  ',
          '      |  ',
          '      |  ',
          '========='
        ],
        3 :[
          '  +---+  ',
          '  |   |  ',
          '  O   |  ',
          ' /|   |  ',
          '      |  ',
          '      |  ',
          '========='
        ],
        2 :[
          '  +---+  ',
          '  |   |  ',
          '  O   |  ',
          ' /|\\  |  ',
          '      |  ',
          '      |  ',
          '========='
        ],
        1 :[
          '  +---+  ',
          '  |   |  ',
          '  O   |  ',
          ' /|\\  |  ',
          ' /    |  ',
          '      |  ',
          '========='
        ],
        0 :[
          '  +---+  ',
          '  |   |  ',
          '  O   |  ',
          ' /|\\  |  ',
          ' / \\  |  ',
          '      |  ',
          '========='
        ],
    }
    with open('hangedman.dat', 'wb') as outfile:
        pickle.dump(hangedman, outfile)

main()