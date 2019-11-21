'''
6. Joe’s Automotive
    Joe’s Automotive performs the following routine maintenance services:
        • Oil change          —   $26.00
        • Lube job            —   $18.00
        • Radiator flush      —   $30.00
        • Transmission flush  —   $80.00
        • Inspection          —   $15.00
        • Muffler replacement —   $100.00
        • Tire rotation       —   $20.00
    Write a GUI program with check buttons that allow the user to select any or all of these
    services. When the user clicks a button the total charges should be displayed.
'''

import tkinter as tk

def main():
    # instantiate the window
    window = tk.Tk()

    # Set the window title and geometry (As Desired)
    window.title('Joe\'s Automotive')
    # window.geometry('400x400')

    # Create the checkbuttons and variables
    var_oil = tk.BooleanVar()
    var_lube = tk.BooleanVar()
    var_radiator = tk.BooleanVar()
    var_transmission = tk.BooleanVar()
    var_inspection = tk.BooleanVar()
    var_muffler = tk.BooleanVar()
    var_tire_rot = tk.BooleanVar()
    var_total = tk.StringVar()
    var_total.set(0.00)
    final_row = 0

    jobs_dict = {
        'Oil Change:' : {'cost' : 26.00, 'ck_var': var_oil},
        'Lube Job:' : {'cost' : 18.00, 'ck_var': var_lube},
        'Radiator Flush:' : {'cost' : 30.00, 'ck_var': var_radiator},
        'Transmission Flush:' : {'cost' : 80.00, 'ck_var': var_transmission},
        'Inspection:' : {'cost' : 15.00, 'ck_var': var_inspection},
        'Muffler Replacement:' : {'cost' : 100.00, 'ck_var': var_muffler},
        'Tire Rotation:' : {'cost' : 20.00, 'ck_var': var_tire_rot}
    }

    # define the total function
    def calc_total():
        # initialize a total accumalator
        total = 0
        # Iterate through all possible jobs
        for job in jobs_dict.keys():
            # if job's checkbutton variable is set to 1
            if jobs_dict[job]['ck_var'].get() == 1:
                # add the job's cost to the total
                total += jobs_dict[job]['cost']
        # set the total vaiable to the total
        var_total.set(f'Total:\t${total:.2f}')
    
    # create an empty list to store all of the created checkbuttons
    all_checkbuttons = []

    # Create a checkbutton for each job
    for job in jobs_dict.keys():
        if len(job) > 15:
            checkbutton = tk.Checkbutton(text='{} \t${:.2f}'.format(job, jobs_dict[job]['cost']), variable=jobs_dict[job]['ck_var'], onvalue=1, offvalue=0, width=30, command=calc_total, anchor='w')
        else:
            checkbutton = tk.Checkbutton(text='{} \t\t${:.2f}'.format(job, jobs_dict[job]['cost']), variable=jobs_dict[job]['ck_var'], onvalue=1, offvalue=0, width=30, command=calc_total, anchor='w')
        all_checkbuttons.append(checkbutton)

    # place the checkbuttons on the gui grid and configure as necessary
    for r, button in enumerate(all_checkbuttons):
        button.grid(row=r, column=0, padx=5)
        final_row = r + 1

    # create the total label
    label_total = tk.Label(textvariable=var_total)
    label_total.grid(row=final_row, column=0)

    # call the window mainloop
    window.mainloop()
# Call the main function
main()
