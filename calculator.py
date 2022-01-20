class calculator():
    
    ALARM = False

    def PROFITLOSS_NET(purchased, price):
        return int(price-purchased)
    
    def PROFITLOSS_PERCENT(purchased, price):
        check = price - purchased
        
        if check < 0:
            #change color to red
            ALARM = True
            return -(check/purchased)
        else:
            #change color to green
            return check/purchased
    
    def STOPCALL(purchased, price):
        #could have these values pass through as well
        SELL_1 = 0.25
        SELL_2 = 0.3
        SELL_3 = 0.35
        #could have percent pass through instead of purchase/price
        percent = (price - purchased) / purchased
        #simple check for stop calls
        if percent >= SELL_3:
            print("The percent " + str(percent * 100) + "% is greater than your third sell option: " + str(SELL_3 * 100) + "%.")
        elif percent >= SELL_2:
            print("The percent " + str(percent * 100) + "% is greater than your second sell option: " + str(SELL_2 * 100) + "%.")
        elif percent >= SELL_1:
            print("The percent " + str(percent * 100) + "% is greater than your first sell option: " + str(SELL_1 * 100) + "%.")
        else:
            print("No sell options have been met with this coin")    

profit = calculator.PROFITLOSS_NET(100, 50)
print(profit)