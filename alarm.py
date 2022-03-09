""" Module that sets an alarm as transaction data """
class Alarm:

    def __init__(self, crypto_name, condition, frequency, price, alert_name):
        self.crypto_name = crypto_name
        self.condition = condition
        self.price = price
        self.frequency = frequency
        self.alert_name = alert_name
        self.has_alert_name()

    def has_alert_name(self):
        """
        gives a default alert name for the alarm having the form ['cryptocurrency' alarm: condition] if not given one
        """
        if self.alert_name == "":
            self.alert_name = self.crypto_name + " alarm : " + str(self.condition) + str(self.price)

    def return_alert(self):
        """ Stores the alert into a dictionary with a key where it's values is set to [coin name + condition] """
        key = str(self.crypto_name + str(self.condition)+str(self.price))
        alerts_dictonary = {}
        if key not in alerts_dictonary:
            alerts_dictonary[key] = {self.crypto_name, self.condition, self.price, self.frequency, self.alert_name}
        return alerts_dictonary

def main():
    crypto = Alarm("Bitcoin", ">", "One Time", "3293.03", "")
    print(crypto.alert_name)

if __name__ == "__main__":
    main()