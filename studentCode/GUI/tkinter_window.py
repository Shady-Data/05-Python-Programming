# Access tkinter
import tkinter as tk

# instantiate a tkinter object
window = tk.Tk()

# Set the title for your window
window.title("First tkinter app")

# Set the size of your window
window.geometry('400x400')

# Adding a label
title = tk.Label(text = "Hello world! This font is better", font=('Times New Roman', 24))

# grid() tells you where you want the label, (0,0) is default
title.grid(column=0, row=0)

# Adding a button
button1 = tk.Button(text = 'Click me', bg='red')
button1.grid(column=0, row=1, pady=5)

# Adding an Entry
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2, pady=5)

# Text field
text_field = tk.Text(master=window, height=10, width=30)
text_field.grid(column=0, row=3)

# pack() essentially just throws things in where they fit
# title.pack()

# The opens your window, this is like calling your "function"
# Everything you do must be between this and instantiating your window
# This is always at the bottom.
# Continuoulsy puts the window in a loop to keep it open
window.mainloop()