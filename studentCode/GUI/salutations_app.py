# The salutations app will take in a name and randomly generate a greeting

import random
import tkinter as tk

# Window
window = tk.Tk()
window.title('Salutations')
window.geometry('400x400')

# Functions
def phrase_generator():
    # Create a list of phrases
    phrases = ['Hello', 'What\'s up', 'Howdy', 'Aloha']
    # get name from entry1 field
    name = str(entry1.get())

    return random.choice(phrases) + ' ' + name

def phrase_display():
    # Get greeting from a phrase generator
    greeting = phrase_generator()

    # This creates a text field with our greeting
    greeting_display = tk.Text(master=window, height=10, width=30)
    greeting_display.grid(column=0, row=4)

    greeting_display.insert(tk.END, greeting)
    # configure state='disabled' for text field to prevent user input
    # greeting_display.configure(state='disabled')

# Label
label1 = tk.Label(text='How you doin')
label1.grid(column=0, row=0)

label2 = tk.Label(text='What is your name?')
label2.grid(column=0, row=1)

# Entry
# No arguments cause we want to get user input
entry1 = tk.Entry()
entry1.grid(column=0, row=2, pady=5)

# Button
button1 = tk.Button(text='Click me!', command=phrase_display)
button1.grid(column=0, row=3)

window.mainloop()