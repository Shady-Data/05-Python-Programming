'''
2. Latin Translator
    Look at the following list of Latin words and their meanings.
        Latin       English
        sinister    left
        dexter      right
        medium      center
    Write a GUI program that translates the Latin words to English. The window should have
    three buttons, one for each Latin word. When the user clicks a button, the program displays 
    the English translation in a label.
'''

import tkinter as tk
from functools import partial

def main():
    # Instantiate the window
    window = tk.Tk()

    # set the window geometry and title
    window.geometry('400x400')
    window.title('Latin Translator')

    # define the function to show the info
    def display_English(p_latin):
        # def blank labels to generate from for the dictionary
        labelLeft = None
        labelRight = None
        labelCenter = None
        # Define a translation dictionary with the Latin words as a key
        translation = {
            'sinister' : {'English': 'left', 'label' : labelLeft, 'col' : 0},
            'dexter' : {'English': 'right', 'label' : labelRight, 'col' : 2},
            'medium' : {'English': 'center', 'label' : labelCenter, 'col' : 1}
        }
        # prepare the label to display
        translation[p_latin]['label'] = tk.Label(master=window, text=translation[p_latin]['English'])
        translation[p_latin]['label'].grid(column=translation[p_latin]['col'], row=3)

    # build a title header label for the window
    titleLatin = tk.Label(text='Latin')
    titleLatin.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
    titleEnglish = tk.Label(text='English')
    titleEnglish.grid(row=2, column=1, padx=5, pady=5, sticky='nsew')

    # Build the buttons that calls the display translation function when clicked
    buttonleft = tk.Button(text='sinister', command=partial(display_English, 'sinister'))
    buttonleft.grid(column=0, row=1, padx=10, pady=10)
    buttoncenter = tk.Button(text='medium', command=partial(display_English, 'medium'))
    buttoncenter.grid(column=1, row=1, padx=10, pady=10)
    buttonright = tk.Button(text='dexter', command=partial(display_English, 'dexter'))
    buttonright.grid(column=2, row=1, padx=10, pady=10)


    # call the window mainloop function
    window.mainloop()

# Call the main function
main()