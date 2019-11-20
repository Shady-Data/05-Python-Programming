'''
1. Name and Address
    Write a GUI program that displays your name and address when a button is clicked. 
    When the user clicks the Show Info button, the program should display your name and
    address. Mess with the display to make it look neat.
'''

import tkinter as tk

def main():
    # Instantiate the window
    window = tk.Tk()

    # set the window geometry and title
    window.geometry('400x400')
    window.title('Contact Information')

    # define the function to show the info
    def display_info():
        # set the information
        name = 'Robert Chunn'
        address = '*REDACTED*'
        # build the return Text Fields
        contact = tk.Text(master=window, height=4, width=20)
        contact.grid(column=1, row=4, columnspan=4, padx=5)
        contact.insert(tk.END, 'Name: ' + name + '\n' + 'Address: ' + address)
        # configure the Text field to not allow user input
        contact.configure(state='disabled')

    # Build the button that calls the display window function when clicked
    button = tk.Button(text='Show Info', command=display_info)
    button.grid(column=0, row=1, columnspan=5, padx=40, pady=10)


    # call the window mainloop function
    window.mainloop()

# Call the main function
main()
    
