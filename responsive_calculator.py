""" Module to calculate the percent difference based off user input, calculating in real time. """

import tkinter as tk
 
class ResponsiveCalculator(tk.Tk):
    
    def __init__(self):
        # Creation of the text box variables
        self.initial_price = tk.StringVar()
        self.final_price = tk.StringVar()
        self.percent_difference = tk.StringVar()
        self.raw_difference = tk.StringVar()
    
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

                    # Adjust variables
                    self.initial_price.set(str("{:.2f}".format(initial_price_input)))
                    self.final_price.set(str("{:.2f}".format(final_price_input)))
                    self.percent_difference.set(str("{:.2f}".format(percent_difference_result)))
                    self.raw_difference.set(str("{:.2f}".format(raw_difference_result)))

                # Initial Price & Percent Difference
                percent_difference_input = self.percent_difference.get()
                if percent_difference_input != "":
                    percent_difference_input = float(percent_difference_input)

                    final_price_result = initial_price_input + ((percent_difference_input/100) * initial_price_input)
                    raw_difference_result = final_price_result - initial_price_input
                   
                    # Adjust variables
                    self.initial_price.set(str("{:.2f}".format(initial_price_input)))
                    if final_price_result < 0.0:
                        self.final_price.set('Error')
                    else:     
                        self.final_price.set(str("{:.2f}".format(final_price_result)))
                    self.percent_difference.set(str("{:.2f}".format(percent_difference_input)))
                    self.raw_difference.set(str("{:.2f}".format(raw_difference_result)))

                # Initial Price & Raw Difference
                raw_difference_input = self.raw_difference.get()
                if raw_difference_input != "":
                    raw_difference_input = float(raw_difference_input)

                    final_price_result = initial_price_input + raw_difference_input
                    percent_difference_result = 100 * (final_price_result - initial_price_input) / initial_price_input

                    # Adjust price values
                    self.initial_price.set(str("{:.2f}".format(initial_price_input)))
                    if final_price_result < 0.0:
                        self.final_price.set('Error')
                    else:     
                        self.final_price.set(str("{:.2f}".format(final_price_result)))
                    self.percent_difference.set(str("{:.2f}".format(percent_difference_result)))
                    self.raw_difference.set(str("{:.2f}".format(raw_difference_input)))

    
    
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


                        # Adjust variables   
                        self.initial_price.set(str("{:.2f}".format(initial_price_input))) 
                        self.final_price.set(str("{:.2f}".format(final_price_input)))
                        self.percent_difference.set(str("{:.2f}".format(percent_difference_result)))
                        self.raw_difference.set(str("{:.2f}".format(raw_difference_result)))
            
            #Final Price & Percent Difference
            percent_difference_input = self.percent_difference.get()
            if percent_difference_input != "":
                percent_difference_input = float(percent_difference_input)

                initial_price_result = final_price_input / ((percent_difference_input/100) + 1)
                raw_difference_result = final_price_input - initial_price_result

                # Adjust variables
                if initial_price_result < 0.0:
                    self.initial_price = 'Error'
                else:     
                    self.initial_price.set(str("{:.2f}".format(initial_price_result))) 
                self.final_price.set(str("{:.2f}".format(final_price_input)))
                self.percent_difference.set(str("{:.2f}".format(percent_difference_input)))
                self.raw_difference.set(str("{:.2f}".format(raw_difference_result)))
            
            # Final Price & Raw Input
            raw_difference_input = self.raw_difference.get()
            if raw_difference_input != "":
                raw_difference_input = float(raw_difference_input)

                initial_price_result = final_price_input - raw_difference_input
                percent_difference_result = 100 * (final_price_input - initial_price_result) / initial_price_result

                # Adjust variables
                if initial_price_result < 0.0:
                    self.initial_price = 'Error'
                else:     
                    self.initial_price.set(str("{:.2f}".format(initial_price_result))) 
                self.final_price.set(str("{:.2f}".format(final_price_input)))
                self.percent_difference.set(str("{:.2f}".format(percent_difference_result)))
                self.raw_difference.set(str("{:.2f}".format(raw_difference_input)))
               
                
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

                    # Adjust variables
                    self.initial_price.set(str("{:.2f}".format(initial_price_input))) 
                    if final_price_result < 0.0:
                        self.final_price.set('Error')
                    else:     
                        self.final_price.set(("{:.2f}".format(final_price_result)))
                    self.percent_difference.set(str("{:.2f}".format(percent_difference_input)))
                    self.raw_difference.set(str("{:.2f}".format(raw_difference_result)))
            
            # Percent Difference & Final Price
            final_price_input = self.final_price.get()
            if final_price_input != "":
                final_price_input = float(final_price_input)

                initial_price_result = final_price_input / ((percent_difference_input/100) + 1)
                raw_difference_result = final_price_input - initial_price_result

                # Adjust variables
                if initial_price_result < 0.0:
                    self.initial_price.set('Error')
                else:     
                    self.initial_price.set(str("{:.2f}".format(initial_price_result)))    
                self.final_price.set(str("{:.2f}".format(final_price_input)))
                self.percent_difference.set(str("{:.2f}".format(percent_difference_input)))
                self.raw_difference.set(str("{:.2f}".format(raw_difference_result)))

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

                    # Adjust variables
                    self.initial_price.set(str("{:.2f}".format(initial_price_input))) 
                    if final_price_result < 0.0:
                        self.final_price.set('Error')
                    else:     
                        self.final_price.set(str("{:.2f}".format(final_price_result)))
                    self.percent_difference.set(str("{:.2f}".format(percent_difference_result)))
                    self.raw_difference.set(str("{:.2f}".format(raw_difference_input)))
            
            # Raw Difference & Final Price 
            final_price_input = self.final_price.get()
            if final_price_input != "":
                final_price_input = float(final_price_input)

                initial_price_result = final_price_input - raw_difference_input
                percent_difference_result = 100 * (final_price_input - initial_price_result) / initial_price_result

                # Adjust variables
                if initial_price_result < 0.0:
                    self.initial_price = 'Error'
                else:     
                    self.initial_price.set(str("{:.2f}".format(initial_price_result)))    
                self.final_price.set(str("{:.2f}".format(final_price_input)))
                self.percent_difference.set(str("{:.2f}".format(percent_difference_result)))
                self.raw_difference.set(str("{:.2f}".format(raw_difference_input)))

         # Raw Difference and Percent Difference do not allow for a proper answer.
            
    def return_labels(self):
        initial_price_input = self.initial_price
        final_price_input = self.final_price
        percent_difference = self.percent_difference
        raw_difference = self.raw_difference
        return initial_price_input, final_price_input, percent_difference, raw_difference
    
def main():
    app = ResponsiveCalculator()
    app.mainloop()

if __name__ == "__main__":
    main()
