""" Simple file that computes the percent increase / decrease of the values """


class PercentChange:
    def __init__(self, initial_price, final_price):
        """
        Parameterized constructor which initializes the initial, and final prices passed

        :param initial_price: initial price of the asset
        :param final_price: current price of the asset
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
            return "+{0:.2f}%".format(percent_increase_result)
        else:
            return "{0:.2f}%".format(percent_increase_result)

    def price_difference(self):
        """
        Returns the difference between the values

        :return: the difference between two numbers
        """
        return abs(self.initial_price - self.final_price)


def main():
    """ """
    #  percent_change = PercentChange()


if __name__ == '__main__':
    main()
