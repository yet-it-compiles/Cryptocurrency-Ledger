import psycopg2
from psycopg2 import Error
import manual_transaction
from manual_transaction import *
import weighted_calculator
from weighted_calculator import update_average


class Database:

    def __init__(self, username) -> object:
        self.username = username
        self.session_start_id = 0
        self.transaction_id = 0
        self.all_transactions = []
        self.current_holdings = {}
        self.pull_transactions()

    @staticmethod
    def connect():
        connection = psycopg2.connect(host="ec2-3-232-22-121.compute-1.amazonaws.com",
                                      database="dilabshsjveo3",
                                      user="ogjzilgdyfltod",
                                      password="2a5fff6b7763149071662013def40f9cb2f9f6c8eef3e719f286d8e499ea8471"
                                      )
        return connection

    @staticmethod
    def adduser(username, email, password):
        """
        Adds the user for the first time
        """
        if Database.checkUsername(username):
            "username is taken"
            return
        is_connected = Database.connect()
        try:

            executes_query = is_connected.cursor()
            postgres_insert_query = "INSERT INTO users Values( %s, %s, %s)"
            record_to_insert = (username, email, password)

            executes_query.execute(postgres_insert_query, record_to_insert)

            is_connected.commit()

            count = executes_query.rowcount
            print(count, "Record inserted successfully into mobile table")

        except(Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)

        finally:
            # closing database is_connected.
            if is_connected:
                executes_query.close()
                is_connected.close()

    @staticmethod
    def get_pass(username):
        is_connected = Database.connect()
        try:

            executes_query = is_connected.cursor()
            postgres_select_query = "Select pass FROM users WHERE username = %s"

            executes_query.execute(postgres_select_query, (username,))

            result = executes_query.fetchone()

            return result

        except(Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)

        finally:
            # closing database is_connected.
            if is_connected:
                executes_query.close()
                is_connected.close()

    @staticmethod
    def checkUsername(name) -> bool:
        """
        Checks Database for the username provided. Static because it needs to be accessed from outside a database object
        returns true if is in the database
        param:  NAME: username as a string
        return type: boolean
        """
        connection = Database.connect()
        try:

            cursor = connection.cursor()
            postgres_select_query = "Select username FROM users WHERE  username = %s"

            cursor.execute(postgres_select_query, (name,))

            result = cursor.fetchone()
            if result is None:
                return False
            return True
        except(Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()

    def push_transactions(self):
        """
        takes the updated transaction lists and updates the database upon program close
        param: database object.
        return type: boolean
        """
        connection = Database.connect()
        success = True
        try:
            cursor = connection.cursor()
            postgres_query = "INSERT INTO allTransactions VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            for transaction in self.all_transactions:
                if transaction.id > self.session_start_id:
                    cusrsor.execute(postgres_query, transaction.id, self.username, transaction.crypto_name,
                                    transaction.is_buy,
                                    transaction.current_price, transaction.num_coins_trading, transaction.target,
                                    transaction.fee, transaction.utc_date_time)

                connection.commit()
        except(Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)
            success = False

        finally:
            # closing database is_connected.
            if is_connected:
                executes_query.close()
                is_connected.close()

        return success

    def pull_transactions(self):
        """
        connects to the database and appends the list of all transactions
        param: self
        return: void
        """
        connection = Database.connect()
        try:
            cursor = connection.cursor()
            postgres_select_query = "Select * FROM allTransactions WHERE  username = %s"
            cursor.execute(postgres_select_query, (self.username,))
            result = cursor.fetchall()
            """
            "Id = ", row[0]
            "username = ", row[1]
            "coin_name  = ", row[2]
            "buy_trade = ", row[3]
            "price = ", row[4]
            "amount  = ", row[5]
            "target = ", row[6]
            "Fee = ", row[7]
            "time  = ", row[8]
            """
            if result is None:
                return
            for row in result:
                transaction = ManualTransaction(row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                self.all_transactions.append(transaction)
                if row[0] > self.transaction_id:
                    self.transaction_id = row[0]
                    self.session_start_id = row[0]

        except(Exception, psycopg2.Error) as error:
            print("Failed to retrieve record into mobile table", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()

    def get_coin_transactions(self, coin_name):
        """
        Gets all the transactions related to the current coin
        :param coin_name: The name of the coin that is being accessed
        :return: a list of all the transactions with the coin
        """
        result = []
        for row in self.all_transactions:
            if row.coin_name == coin_name:
                result.append(row)
        return result

    """
    Current Holding dictionary:  (Dictionary of Dictionaries)
    "coin_name": {avg_price: int, amount: int, target: int}
    """

    def push_current(self):
        """
        Takes the dictionary and updates all the fields in the
        returns true if successfully inserted
        return type: boolean
        """
        connection = Database.connect()
        success = True
        try:
            cursor = connection.cursor()
            postgres_query = "UPDATE currentHoldings SET avg_price = %s, amount = %s, target = %s WHERE username = %s " \
                             "AND coin_name = %s "
            for key in self.current_holdings:
                cursor.execute(postgres_query, self.current_holdings[key]['avg_price'],
                               self.current_holdings[key]['amount'],
                               self.current_holdings[key]['target'],
                               self.username, key)

            connection.commit()
        except(Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)
            success = False

        finally:
            # closing database is_connected.
            if is_connected:
                executes_query.close()
                is_connected.close()

        return success

    def get_current(self):
        connection = Database.connect()
        try:
            cursor = connection.cursor()
            postgres_query = "SELECT * FROM currentHoldings"
            cursor.execute(postgres_select_query, (self.username,))
            result = cursor.fetchall()
            """
            username = row[0]
            coin_name = row[1]
            avg_price = row[2]
            amount = row[3]
            target = row[4]
            """
            for row in result:
                self.current_holdings[row[1]]['avg_price'] = row[2]
                self.current_holdings[row[1]]['amount'] = row[3]
                self.current_holdings[row[1]]['target'] = row[4]
        except(Exception, psycopg2.Error) as error:
            print("Failed to retrieve record into mobile table", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()

    def add_transaction(self, transaction):
        # all Transactions update
        self.transaction_id += 1
        transaction.id = self.transaction_id
        self.all_transactions.append(transaction)

        # Portfolio Update
        coin_name = transaction.crypto_name
        new_purchase = transaction.current_price
        new_amt = transaction.num_coins_trading
        if coin_name in self.current_holdings:
            current_avg = self.current_holdings[coin_name]["avg_price"]
            current_amt = self.current_holdings[coin_name]["amount"]

            new_avg = update_average(current_avg, current_amt, new_purchase, new_amt)

            if transaction.is_buy:
                current_amt += new_amt
            else:
                current_amt -= new_amt
            self.current_holdings[coin_name]['avg_price'] = new_avg
            self.current_holdings[coin_name]['amount'] = current_amt
            self.current_holdings[coin_name]['target'] = transaction.target
        else:
            self.current_holdings[coin_name]['avg_price'] = new_purchase
            self.current_holdings[coin_name]['amount'] = new_amt
            self.current_holdings[coin_name]['target'] = transaction.target




"""

def main():
    test = Database("admin")

    print(test.transaction_id)
    print(test.all_transactions)


"""
