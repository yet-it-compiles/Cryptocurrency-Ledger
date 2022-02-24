import psycopg2
from psycopg2 import Error


class Database:

    def __init__(self, username):
        self.username = username
        self.all_transactions = self.pull_transactions()

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
    def checkUsername(name):
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

def pull_transactions(self):
    connection = Database.connect()
    try:
        cursor = connection.cursor()
        postgres_select_query = "Select * FROM transactions WHERE  username = %s"
        cursor.execute(postgres_select_query, (username,))
        result = cursor.fetchall()
        return result
    except(Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

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
    res
    for x in all_transactions:
        if  x == coin_name:
            pass
def push_current(self):
    pass
def get_current(self):
    pass