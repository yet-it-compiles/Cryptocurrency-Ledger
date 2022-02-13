""" Module to calculate the percent difference based off user input, calculating in real time. """

import tkinter as tk
 
class responsiveCalculator(tk.Tk):
    
    # Creation of the window that holds the calculator
    def __init__(self):
        super().__init__()
        self.title('Responsive Calculator')
        self.resizable(False, False)
        self.geometry("600x200")

        # Creation of the text box variables
        self.initial_price = tk.StringVar()
        self.final_price = tk.StringVar()
        self.percent_difference = tk.StringVar()
        self.raw_difference = tk.StringVar()

        # Trace of the text box variables
        self.initial_price.trace('w', self.calculate_initial_price)
        self.final_price.trace('w', self.calculate_final_price)
        self.percent_difference.trace('w', self.calculate_percent_difference)
        self.raw_difference.trace('w', self.calculate_raw_difference)
 
        self.create_widgets()

    # Creation of the text boxes 
    def create_widgets(self):
        self.initial_price_label = tk.Label(self, text = "Enter Initial Price:")
        self.initial_price_label.grid(column = 0, row = 0)
        self.initial_price_entry = tk.Entry(self, textvariable = self.initial_price)
        self.initial_price_entry.grid(column = 1, row = 0)
        self.initial_price_entry.focus()
        self.initial_price_calc = tk.Label(self, text = "")
        self.initial_price_calc.grid(column = 2, row = 0)

        self.final_price_label = tk.Label(self, text = "Enter Final Price:")
        self.final_price_label.grid(column = 0, row = 1)
        self.final_price_entry = tk.Entry(self, textvariable = self.final_price)
        self.final_price_entry.grid(column = 1, row = 1)
        self.final_price_calc = tk.Label(self, text = "")
        self.final_price_calc.grid(column = 2, row = 1)

        self.percent_difference_label = tk.Label(self, text = "Enter Percent Difference:")
        self.percent_difference_label.grid(column = 0, row = 2)
        self.percent_difference_entry = tk.Entry(self, textvariable = self.percent_difference)
        self.percent_difference_entry.grid(column = 1, row = 2)
        self.percent_difference_calc = tk.Label(self, text = "")
        self.percent_difference_calc.grid(column = 2, row = 2)

        self.raw_difference_label = tk.Label(self, text = "Enter Raw Difference:")
        self.raw_difference_label.grid(column = 0, row = 3)
        self.raw_difference_entry = tk.Entry(self, textvariable = self.raw_difference)
        self.raw_difference_entry.grid(column = 1, row = 3)
        self.raw_difference_calc = tk.Label(self, text = "")
        self.raw_difference_calc.grid(column = 2, row = 3)

    # From perspective of the Initial Price
    def calculate_initial_price(self, *args):
        initial_price_input = self.initial_price.get()
 
        if initial_price_input != "":
            if float(initial_price_input) > 0.0:
                initial_price_input = float(initial_price_input)

                # Initial Price & Final Price
                final_price_input = self.final_price.get()
                if final_price_input != "":
                    final_price_input = float(final_price_input)
                    
                    percent_difference_result = 100 * (final_price_input - initial_price_input) / initial_price_input
                    raw_difference_result = final_price_input - initial_price_input

                    # Print all four to the labels
                    self.initial_price_calc['text'] = '$' + str(initial_price_input)
                    self.final_price_calc['text'] = '$' + str(final_price_input)
                    self.percent_difference_calc['text'] = str(percent_difference_result) + '%'
                    self.raw_difference_calc['text'] = '$' + str(raw_difference_result)

                # Initial Price & Percent Difference
                percent_difference_input = self.percent_difference.get()
                if percent_difference_input != "":
                    percent_difference_input = float(percent_difference_input)

                    final_price_result = initial_price_input + ((percent_difference_input/100) * initial_price_input)
                    raw_difference_result = final_price_result - initial_price_input

                    # Print all four to the labels
                    self.initial_price_calc['text'] = '$' + str(initial_price_input)
                    if final_price_result < 0.0:
                        self.final_price_calc['text'] = 'Error - Final Price cannot be less than Zero'
                    else: 
                        self.final_price_calc['text'] = '$' + str(final_price_result)
                    self.percent_difference_calc['text'] = str(percent_difference_input) + '%'
                    self.raw_difference_calc['text'] = '$' + str(raw_difference_result)

                # Initial Price & Raw Difference
                raw_difference_input = self.raw_difference.get()
                if raw_difference_input != "":
                    raw_difference_input = float(raw_difference_input)

                    final_price_result = initial_price_input + raw_difference_input
                    percent_difference_result = 100 * (final_price_result - initial_price_input) / initial_price_input

                    # Print all four to the labels
                    self.initial_price_calc['text'] = '$' + str(initial_price_input)
                    if final_price_result < 0.0:
                        self.final_price_calc['text'] = 'Error - Final Price cannot be less than Zero'
                    else: 
                        self.final_price_calc['text'] = '$' + str(final_price_result)
                    self.percent_difference_calc['text'] = str(percent_difference_result) + '%'
                    self.raw_difference_calc['text'] = '$' + str(raw_difference_input)

    
    
    # From perspective of the Final Price
    def calculate_final_price(self, *args):
        final_price_input = self.final_price.get()
 
        if final_price_input != "":
            if float(final_price_input) > 0.0:
                final_price_input = float(final_price_input)

                # Final Price & Initial Price
                initial_price_input = self.initial_price.get()
                if initial_price_input != "":
                    if float(initial_price_input) > 0.0:
                        initial_price_input = float(initial_price_input)

                        percent_difference_result = 100 * (final_price_input - initial_price_input) / initial_price_input
                        raw_difference_result = final_price_input - initial_price_input

                        # Print all four to the labels
                        self.initial_price_calc['text'] = '$' + str(initial_price_input)
                        self.final_price_calc['text'] = '$' + str(final_price_input)
                        self.percent_difference_calc['text'] = str(percent_difference_result) + '%'
                        self.raw_difference_calc['text'] = '$' + str(raw_difference_result)
            
            #Final Price & Percent Difference
            percent_difference_input = self.percent_difference.get()
            if percent_difference_input != "":
                percent_difference_input = float(percent_difference_input)

                initial_price_result = final_price_input / ((percent_difference_input/100) + 1)
                raw_difference_result = final_price_input - initial_price_result

                # Print all four to the labels
                if initial_price_result < 0.0:
                    self.initial_price_calc['text'] = 'Error - Initial Price cannot be less than Zero'
                else:
                    self.initial_price_calc['text'] = '$' + str(initial_price_result)
                self.final_price_calc['text'] = '$' + str(final_price_input)
                self.percent_difference_calc['text'] = str(percent_difference_input) + '%'
                self.raw_difference_calc['text'] = '$' + str(raw_difference_result)
            
            # Final Price & Raw Input
            raw_difference_input = self.raw_difference.get()
            if raw_difference_input != "":
                raw_difference_input = float(raw_difference_input)

                initial_price_result = final_price_input - raw_difference_input
                percent_difference_result = 100 * (final_price_input - initial_price_result) / initial_price_result

                # Print all four to the labels
                if initial_price_result < 0.0:
                    self.initial_price_calc['text'] = 'Error - Initial Price cannot be less than Zero'
                else:
                    self.initial_price_calc['text'] = '$' + str(initial_price_result)
                self.final_price_calc['text'] = '$' + str(final_price_input)
                self.percent_difference_calc['text'] = str(percent_difference_result) + '%'
                self.raw_difference_calc['text'] = '$' + str(raw_difference_input)
               
                
    # From perspective of the Percent Difference
    def calculate_percent_difference(self, *args):
        percent_difference_input = self.percent_difference.get()
 
        if percent_difference_input != "":
            percent_difference_input = float(percent_difference_input)

            # Percent Difference & Initial Price
            initial_price_input = self.initial_price.get()
            if initial_price_input != "":
                if float(initial_price_input) > 0.0:
                    initial_price_input = float(initial_price_input)

                    final_price_result = initial_price_input + ((percent_difference_input/100) * initial_price_input)
                    raw_difference_result = final_price_result - initial_price_input

                    # Print all four to the labels
                    self.initial_price_calc['text'] = '$' + str(initial_price_input)
                    
                    if final_price_result < 0.0:
                        self.final_price_calc['text'] = 'Error - Final Price cannot be less than Zero'
                    else: 
                        self.final_price_calc['text'] = '$' + str(final_price_result)

                    self.percent_difference_calc['text'] = str(percent_difference_input) + '%'
                    self.raw_difference_calc['text'] = '$' + str(raw_difference_result)
            
            # Percent Difference & Final Price
            final_price_input = self.final_price.get()
            if final_price_input != "":
                final_price_input = float(final_price_input)

                initial_price_result = final_price_input / ((percent_difference_input/100) + 1)
                raw_difference_result = final_price_input - initial_price_result

                if initial_price_result < 0.0:
                    self.initial_price_calc['text'] = 'Error - Initial Price cannot be less than Zero'
                else:
                    self.initial_price_calc['text'] = '$' + str(initial_price_result)
                
                self.final_price_calc['text'] = '$' + str(final_price_input)
                self.percent_difference_calc['text'] = str(percent_difference_input) + '%'
                self.raw_difference_calc['text'] = '$' + str(raw_difference_result)

            # Percent Difference and Raw Difference do not allow for a proper answer.
         
        
    
    # From perspective of the Raw Difference
    def calculate_raw_difference(self, *args):
        raw_difference_input = self.raw_difference.get()
 
        if raw_difference_input != "":
            raw_difference_input = float(raw_difference_input)

            # Raw Difference & Initial Price
            initial_price_input = self.initial_price.get()
            if initial_price_input != "":
                if float(initial_price_input) > 0.0:
                    initial_price_input = float(initial_price_input)

                    final_price_result = initial_price_input + raw_difference_input
                    percent_difference_result = 100 * (final_price_result - initial_price_input) / initial_price_input

                    # Print all four to the labels
                    self.initial_price_calc['text'] = '$' + str(initial_price_input)
                    if final_price_result < 0.0:
                        self.final_price_calc['text'] = 'Error - Final Price cannot be less than Zero'
                    else: 
                        self.final_price_calc['text'] = '$' + str(final_price_result)
                    self.percent_difference_calc['text'] = str(percent_difference_result) + '%'
                    self.raw_difference_calc['text'] = '$' + str(raw_difference_input)
            
            # Raw Difference & Final Price 
            final_price_input = self.final_price.get()
            if final_price_input != "":
                final_price_input = float(final_price_input)

                initial_price_result = final_price_input - raw_difference_input
                percent_difference_result = 100 * (final_price_input - initial_price_result) / initial_price_result

                # Print all four to the labels
                if initial_price_result < 0.0:
                    self.initial_price_calc['text'] = 'Error - Initial Price cannot be less than Zero'
                else:
                    self.initial_price_calc['text'] = '$' + str(initial_price_result)
                self.final_price_calc['text'] = '$' + str(final_price_input)
                self.percent_difference_calc['text'] = str(percent_difference_result) + '%'
                self.raw_difference_calc['text'] = '$' + str(raw_difference_input)

         # Raw Difference and Percent Difference do not allow for a proper answer.
        
    
if __name__ == "__main__":
    app = responsiveCalculator()
    app.mainloop()