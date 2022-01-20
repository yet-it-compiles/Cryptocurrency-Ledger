""" Simple calculator that calculate the percent increase. and decrease between two values """
from pconst import const


class Calculator:
    const.ALARM = False

    def profit_loss_net(self, initial_price, final_price):
        """

        :param final_price:
        :param initial_price:
        :return:
        """
        return int(initial_price - final_price)

    def profit_loss_percent(self, initial_price, final_price):
        """

        :param initial_price:
        :param final_price:
        :return:
        """
        check = final_price - initial_price

        if check < 0:
            # change color to red
            const.ALARM = True
            return -(check / initial_price)
        else:
            # change color to green
            return check / initial_price

    def STOPCALL(self, initial_price, final_price):
        """

        :param initial_price:
        :param final_price:
        :return:
        """
        # could have these values pass through as well
        profit_target_1 = 0.25
        profit_target_2 = 0.3
        profit_target_3 = 0.35
        # could have percent pass through instead of purchase/price
        percent = (final_price - initial_price) / initial_price
        # simple check for stop calls
        if percent >= profit_target_3:
            print("The percent " + str(percent * 100) + "% is greater than your third sell option: " + str(
                profit_target_3 * 100) + "%.")
        elif percent >= profit_target_2:
            print("The percent " + str(percent * 100) + "% is greater than your second sell option: " + str(
                profit_target_2 * 100) + "%.")
        elif percent >= profit_target_1:
            print("The percent " + str(percent * 100) + "% is greater than your first sell option: " + str(
                profit_target_1 * 100) + "%.")
        else:
            print("No sell options have been met with this coin")


profit = Calculator().profit_loss_net(100, 50)
print(profit)
