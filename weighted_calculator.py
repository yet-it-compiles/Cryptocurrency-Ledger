   
def weighted_calculator(weight_list, value_list):
        """
        this calculates the average buy or sell of a user's transactions    
        param weight_list: float array | int array
        param value_list: float array | int array
        param buy_sell: Boolean
        """
        sum = 0
        div = 0

        # calculations for weighted average
        for i in range(len(weight_list)):
            sum = sum + (weight_list[i] * value_list[i])
            div = div + weight_list[i]
        
        return float("{0:.2f}".format(float(sum)/div))

@staticmethod
def update_average(curr_avg, curr_amt, new_purchase, new_amt):
        """
        this method updates the new average price considering the price of the coin
        at the time it was bought
        param curr_avg: float
        param curr_amt: int
        param new_purchase: float
        new_amt: int

        rtype: float
        """

        return float("{0:.2f}".format((curr_avg + new_purchase) / (curr_amt + new_amt)))