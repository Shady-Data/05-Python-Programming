'''
4. Celsius to Fahrenheit
    Write a GUI program that converts Celsius temperatures to Fahrenheit temperatures. The user
    should be able to enter a Celsius temperature, click a button, and then see the equivalent
    Fahrenheit temperature. Use the following formula to make the conversion:
​
        F = (9/5)C + 32
​
    F is the Fahrenheit temperature and C is the Celsius temperature.
'''

import tkinter as tk

def main():
    # instantiate the window
    window = tk.Tk()

    # Set the window title and geometry
    window.title('Calculator: Celcius to Fahrenheit')
    # window.geometry('400x400')

    # define the calc_cel_to_fahr function
    def calc_cel_to_fahr():
        # get the celius entry
        celsius = cel_var.get()
        # calculate the fahrenheit
        fahrenheit = (9/5) * celsius + 32
        # Create a lebel and display the result
        fahr_result = tk.Label(master=window, text=f'{fahrenheit:.1f}°F')
        fahr_result.grid(row=1 , column=1, pady=5)

    # Create labels for headers
    label_celsius = tk.Label(text='Celsius:')
    label_celsius.grid(row=0, column=0, padx=10, pady=20)
    label_fahrenheit = tk.Label(text='Fahrenheit:')
    label_fahrenheit.grid(row=0, column=1, padx=10, pady=20)

    # create the entry box and variable
    cel_var = tk.IntVar()
    entry_celsius = tk.Entry(textvariable=cel_var, justify='center')
    entry_celsius.grid(row=1, column=0, padx=10, pady=5)

    # Create a button to call the calculation function when clicked
    button_calc = tk.Button(text='Calculate Fahrenheit', command=calc_cel_to_fahr)
    button_calc.grid(row=2, column=0, columnspan=2, pady=20)

    # Call the window mainloop
    window.mainloop()
# Call the main function
main()
