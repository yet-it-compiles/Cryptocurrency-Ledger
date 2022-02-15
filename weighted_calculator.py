   
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
