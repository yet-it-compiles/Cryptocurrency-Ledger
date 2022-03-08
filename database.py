""" TODO - Document """
import psycopg2
from manual_transaction import *
from weighted_calculator import update_average


class Database:
    def __init__(self, username):
        self.username = username
        self.session_start_id = 0
        self.transaction_id = 0
        self.all_transactions = []
        self.current_holdings = {}
        self.pull_transactions()
        self.get_current()

    @staticmethod
    def database_connection():
        """
        Returns a new database connection
        """
        is_connected = psycopg2.connect(host="ec2-3-232-22-121.compute-1.amazonaws.com",
                                        database="dilabshsjveo3",
                                        user="ogjzilgdyfltod",
                                        password="2a5fff6b7763149071662013def40f9cb2f9f6c8eef3e719f286d8e499ea8471")
        return is_connected

    @staticmethod
    def adduser(users_username, email, password):
        """
        Adds the user for the first time
        """
        is_connected = Database.database_connection()
        try:

            executes_query = is_connected.cursor()
            postgres_insert_query = "INSERT INTO users Values(%s, %s, %s)"
            record_to_insert = (users_username, email, password)

            executes_query.execute(postgres_insert_query, record_to_insert)

            is_connected.commit()

            row_cursor = executes_query.rowcount
            print(row_cursor, "Record inserted successfully into mobile table")

        except(Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)

        finally:
            # Logic to define is the database is connected, then to close it
            if is_connected:
                executes_query.close()
                is_connected.close()

    @staticmethod
    def get_pass(username):
        is_connected = Database.database_connection()
        try:

            executes_query = is_connected.cursor()
            postgres_select_query = "Select pass FROM users WHERE username = %s"

            executes_query.execute(postgres_select_query, (username,))

            next_query_row = executes_query.fetchone()

            return next_query_row

        except(Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)

        finally:
            # Logic to define is the database is connected, then to close it
            if is_connected:
                executes_query.close()
                is_connected.close()

    @staticmethod
    def checkUsername(users_username) -> bool:
        """
        Checks database for the username provided, and returns true if username exists

        :param users_username: string representation of the users name
        :return: bool
        """
        is_connected = Database.database_connection()
        try:
            cursor = is_connected.cursor()
            postgres_select_query = "Select username FROM users WHERE  username = %s"

            cursor.execute(postgres_select_query, (users_username,))

            result = cursor.fetchone()
            if result is None:
                return False
            else:
                return True
        except(Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)

        finally:
            # closing database connection.
            if is_connected:
                cursor.close()
                is_connected.close()

    def push_transactions(self):
        """
        Retrieves the updated transaction lists then updates the database upon the program being closed

        :return: bool
        """
        is_connected = Database.database_connection()
        is_successful = True

        try:
            cursor = is_connected.cursor()
            postgres_query = "INSERT INTO allTransactions VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            for each_transaction in self.all_transactions:
                if each_transaction.id > self.session_start_id:
                    cursor.execute(postgres_query, each_transaction.id, self.username, each_transaction.crypto_name,
                                   each_transaction.is_buy,
                                   each_transaction.current_price, each_transaction.num_coins_trading
                                   , each_transaction.target, each_transaction.fee, each_transaction.utc_date_time)

                is_connected.commit()
        except(Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)
            is_successful = False

        finally:
            # closing database is_connected.
            if is_connected:
                cursor.close()
                is_connected.close()

        return is_successful

    def pull_transactions(self):
        """
        Connects to the database, and appends the list of all transactions

        id = row[0]        username = row[1]        coin_name  = row[2]        buy_trade = row[3]
        price = row[4]     amount  = row[5]         target = row[6]            Fee = row[7]
        time = row[8]

    :return: an updated database, with a list of all transactions
    """
        is_connected = Database.database_connection()

        try:
            cursor = is_connected.cursor()
            postgres_select_query = "Select * FROM allTransactions WHERE  username = %s"
            cursor.execute(postgres_select_query, (self.username,))

            remaining_query_rows = cursor.fetchall()

            if remaining_query_rows is None:
                pass

            for each_row in remaining_query_rows:
                transaction = ManualTransaction(each_row[0], each_row[2], each_row[3], each_row[4], each_row[5]
                                                , each_row[6], each_row[7], each_row[8])
                self.all_transactions.append(transaction)

                if each_row[0] > self.transaction_id:
                    self.transaction_id = each_row[0]
                    self.session_start_id = each_row[0]

        except(Exception, psycopg2.Error) as error:
            print("Failed to retrieve record into mobile table", error)

        finally:
            # closing database connection.
            if is_connected:
                cursor.close()
                is_connected.close()

    def get_coin_transactions(self, coin_name):
        """
        Retrieves all the transactions related to the current coin

        Current Holding dictionary:  (Dictionary of Dictionaries)
        "coin_name": {avg_price: int, amount: int, target: int}
        
        :param coin_name: The name of the coin that is being accessed
        :return: a list of all the transactions with the coin
        """
        collection_of_coin_names = []

        for each_row in self.all_transactions:
            if each_row.coin_name == coin_name:
                collection_of_coin_names.append(each_row)
        return collection_of_coin_names

    def push_current(self):
        """
        Retrieves the dictionary, and updates all the fields to return true if a successful insert occurred.

        :return: bool
        """
        is_connected = Database.database_connection()
        is_successful = True

        try:
            cursor = is_connected.cursor()
            postgres_query = "UPDATE currentHoldings SET avg_price = %s, amount = %s, target = %s WHERE username = %s " \
                             "AND coin_name = %s "
            for each_key in self.current_holdings:
                cursor.execute(postgres_query, self.current_holdings[each_key]['avg_price'],
                               self.current_holdings[each_key]['amount'],
                               self.current_holdings[each_key]['target'],
                               self.username, each_key)

            is_connected.commit()
        except(Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)
            is_successful = False

        finally:
            # closing database is_connected.
            if is_connected:
                cursor.close()
                is_connected.close()

        return is_successful

    def get_current(self):
        """
        TODO - Document
        username = row[0]            coin_name = row[1]            avg_price = row[2]
        amount = row[3]              target = row[4]
        :return:
        """
        is_connected = Database.database_connection()

        try:
            cursor = is_connected.cursor()
            postgres_query = "SELECT * FROM currentHoldings Where username = %s"
            cursor.execute(postgres_query, (self.username,))
            result = cursor.fetchall()

            for row in result:
                self.current_holdings[row[1]] = {}
                self.current_holdings[row[1]] = {'avg_price': row[2], 'amount': row[3], 'target': row[4]}

        except(Exception, psycopg2.Error) as error:
            print("Failed to retrieve record into mobile table", error)

        finally:
            # closing database connection.
            if is_connected:
                cursor.close()
                is_connected.close()

    def add_transaction(self, transaction):
        """
        TODO - Document
        :param transaction:
        :return:
        """
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

    def get_total_portfolio(self):
        list_of_coins = []
        for key in self.current_holdings:
            list_of_coins.append(key)
        dict_of_prices = GeckoApi.get_prices(list_of_coins)
        total_amount = 0
        for key in self.current_holdings:
            total_amount += self.current_holdings[key]['amount'] * dict_of_prices[key]
        return '{:.2f}'.format(total_amount)

    def get_top_earners(self):
        if len(self.current_holdings) == 0:
            return {}

        list_of_coins = []
        for key in self.current_holdings:
            list_of_coins.append(key)

        dict_of_prices = GeckoApi.get_prices(list_of_coins)
        """
        diction of results: 
        
        (coin_name): [current_price, purchase_price, percent_increased]
        """

        results = {}
        for key in self.current_holdings:

            current_price = dict_of_prices[key]
            avg_buy = self.current_holdings[key]['avg_price']
            percent_change = '{:.2f}'.format((current_price - avg_buy) / avg_buy * 100)
            list_of_values = [current_price, avg_buy, percent_change]
            results[key] = list_of_values

        sorted_dict = sorted(results.items(), key=lambda x: x[1][2], reverse=True)
        return sorted_dict


def main():
    test = Database("hinduhops")
    dict = test.get_top_earners()
    print(dict[1][1])

if __name__ == '__main__':
    main()
