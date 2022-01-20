""" Simple file that computes the percent increase / decrease of the values """


class PercentChange:
    initial_price = -1
    final_price = -1

    def __init__(self, initial_price, final_price):
        """
        Parameterized constructor which initializes the initial, and final prices passed
        """
        self.initial_price = initial_price
        self.final_price = final_price

    def percent_increase(self):
        """
        Returns the percent increase / decrease as a two decimal result, with a green or red color
        :rtype float
        :return: the percent differential
        """
        percent_increase_result = 100 * (self.final_price - self.initial_price) / abs(self.initial_price)

        # Declares ansi escape characters
        green = '\033[92m'
        red = "\033[91m"

        if self.final_price > self.initial_price:
            return green + "+{0:.2f}%".format(percent_increase_result)
        else:
            return red + "{0:.2f}%".format(percent_increase_result)

    def price_difference(self):
        """
        Returns the different between initial - final
        :rtype: int
        :return: the difference between two numbers
        """
        return abs(self.initial_price - self.final_price)


percent_change = PercentChange(30, 1).percent_increase()
price_difference = PercentChange(1, 3).price_difference()
