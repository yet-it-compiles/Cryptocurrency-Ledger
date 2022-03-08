""" Module to calculate the percent difference based off user input, calculating in real time. """

import tkinter as tk
 
class ResponsiveCalculator(tk.Tk):
    
    def __init__(self):
        # Creation of the text box variables
        self.initial_price = tk.StringVar()
        self.final_price = tk.StringVar()
        self.percent_difference = tk.StringVar()
        self.raw_difference = tk.StringVar()

        self.initial_price_answer = tk.StringVar()
        self.final_price_answer = tk.StringVar()
        self.percent_difference_answer = tk.StringVar()
        self.raw_difference_answer = tk.StringVar()
    
    # From perspective of the Initial Price
    def calculate_initial_price(self, *args):
        initial_price_input = self.initial_price.get()
 
        if initial_price_input != "":
            if float(initial_price_input) > 0.0:
                # Initial Price & Final Price
                final_price_input = self.final_price.get()
                if final_price_input != "":
                    self.initial_final(float(initial_price_input), float(final_price_input))

                # Initial Price & Percent Difference
                percent_difference_input = self.percent_difference.get()
                if percent_difference_input != "":
                    self.initial_percent(float(initial_price_input), float(percent_difference_input))

                # Initial Price & Raw Difference
                raw_difference_input = self.raw_difference.get()
                if raw_difference_input != "":
                    self.initial_raw(float(initial_price_input), float(raw_difference_input))

    # From perspective of the Final Price
    def calculate_final_price(self, *args):
        final_price_input = self.final_price.get()
 
        if final_price_input != "":
            # Final Price & Initial Price
            initial_price_input = self.initial_price.get()
            if initial_price_input != "":
                self.initial_final(float(initial_price_input), float(final_price_input))
        
            #Final Price & Percent Difference
            percent_difference_input = self.percent_difference.get()
            if percent_difference_input != "":
                self.final_percent(float(final_price_input), float(percent_difference_input))
            
            # Final Price & Raw Input
            raw_difference_input = self.raw_difference.get()
            if raw_difference_input != "":
                self.final_raw(float(final_price_input), float(raw_difference_input))
                     
    # From perspective of the Percent Difference
    def calculate_percent_difference(self, *args):
        percent_difference_input = self.percent_difference.get()
 
        if percent_difference_input != "":
            # Percent Difference & Initial Price
            initial_price_input = self.initial_price.get()
            if initial_price_input != "":
                self.initial_percent(float(initial_price_input), float(percent_difference_input))
            
            # Percent Difference & Final Price
            final_price_input = self.final_price.get()
            if final_price_input != "":
                self.final_percent(float(final_price_input), float(percent_difference_input))

            # Percent Difference and Raw Difference do not allow for a proper answer.
         
    # From perspective of the Raw Difference
    def calculate_raw_difference(self, *args):
        raw_difference_input = self.raw_difference.get()
 
        if raw_difference_input != "":
            # Raw Difference & Initial Price
            initial_price_input = self.initial_price.get()
            if initial_price_input != "":
                self.initial_raw(float(initial_price_input), float(raw_difference_input))

            # Raw Difference & Final Price 
            final_price_input = self.final_price.get()
            if final_price_input != "":
                self.final_raw(float(final_price_input), float(raw_difference_input))

         # Raw Difference and Percent Difference do not allow for a proper answer.

    # Calculations with user inputs "initial price" and "final price"
    def initial_final(self, initial_price_input, final_price_input):
        if initial_price_input > 0.0:
            if final_price_input > 0.0:
                try:
                    percent_difference_result = 100 * (final_price_input - initial_price_input) / initial_price_input
                    raw_difference_result = final_price_input - initial_price_input
                    self.update_labels(initial_price_input, final_price_input, percent_difference_result, raw_difference_result)
                except Exception as ex:
                    print(ex)
    
    # Calculations with user inputs "initial price" and "percent difference"        
    def initial_percent(self, initial_price_input, percent_difference_input):
        if initial_price_input > 0.0:
            try:
                final_price_result = initial_price_input + ((percent_difference_input/100) * initial_price_input)
                raw_difference_result = final_price_result - initial_price_input
                self.update_labels(initial_price_input, final_price_result, percent_difference_input, raw_difference_result)
            except Exception as ex:
                print(ex)

    # Calculations with user inputs "raw difference" and "percent difference"    
    def initial_raw(self, initial_price_input, raw_difference_input):
        if initial_price_input > 0.0:
            try:
                final_price_result = initial_price_input + raw_difference_input
                percent_difference_result = 100 * (final_price_result - initial_price_input) / initial_price_input
                self.update_labels(initial_price_input, final_price_result, percent_difference_result, raw_difference_input)
            except Exception as ex:
                print(ex)
            
    # Calculatiosn with user inputs "final price" and "percent difference"
    def final_percent(self, final_price_input, percent_difference_input):
        if final_price_input > 0.0:
            try:
                initial_price_result = final_price_input / ((percent_difference_input/100) + 1)
                raw_difference_result = final_price_input - initial_price_result
                self.update_labels(initial_price_result, final_price_input, percent_difference_input, raw_difference_result)
            except Exception as ex:
                    print(ex)

    # Calculations with user inputs "final price" and "raw difference"
    def final_raw(self, final_price_input, raw_difference_input):
        if final_price_input > 0.0:
            try:
                initial_price_result = final_price_input - raw_difference_input
                percent_difference_result = 100 * (final_price_input - initial_price_result) / initial_price_result
                self.update_labels(initial_price_result, final_price_input, percent_difference_result, raw_difference_input)
            except Exception as ex:
                print(ex)
        
    def return_labels(self):
        initial_price_input = self.initial_price
        final_price_input = self.final_price
        percent_difference = self.percent_difference
        raw_difference = self.raw_difference
        return initial_price_input, final_price_input, percent_difference, raw_difference

    def get_color(self):
        try:
            if float(self.percent_difference.get()) < 0.0:
                return 'red'
            else:
                return 'green'
        except Exception as ex:
            print(ex)
            return 'green'

    def update_labels(self, initial, final, percent, raw):
        self.initial_price_answer.set(str("{:.2f}".format(initial)))
        self.final_price_answer.set(str("{:.2f}".format(final)))
        self.percent_difference_answer.set(str("{:.2f}".format(percent)))
        self.raw_difference_answer.set(str("{:.2f}".format(raw)))

def main():
    app = ResponsiveCalculator()
    app.mainloop()

if __name__ == "__main__":
    main()
