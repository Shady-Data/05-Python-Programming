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
    window.geometry('400x400')

    # define the calc_cel_to_fahr function
    def calc_cel_to_fahr():
        # get the celius entry
        celsius = cel_var.get()
        # calculate the fahrenheit
        fahrenheit = (9/5) * celsius + 32
        # Create a lebel and display the result
        fahr_result = tk.Label(text=f'{fahrenheit:.1f}°F')
        fahr_result.grid(row=1 , column=1, pady=10)
