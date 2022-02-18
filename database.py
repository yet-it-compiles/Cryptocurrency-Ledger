import psycopg2
from psycopg2 import Error


class Database:

    def __init__(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password


    @staticmethod
    def adduser(username, email, password):
        """
        Adds the user for the first time
        """

        try:
            is_connected = psycopg2.connect(host="ec2-3-232-22-121.compute-1.amazonaws.com",
                                          database="dilabshsjveo3",
                                          user="ogjzilgdyfltod",
                                          password="2a5fff6b7763149071662013def40f9cb2f9f6c8eef3e719f286d8e499ea8471"
                                          )

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

        try:
            is_connected = psycopg2.connect(host="ec2-3-232-22-121.compute-1.amazonaws.com",
                                          database="dilabshsjveo3",
                                          user="ogjzilgdyfltod",
                                          password="2a5fff6b7763149071662013def40f9cb2f9f6c8eef3e719f286d8e499ea8471"
                                          )
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
        try:
            connection = psycopg2.connect(host="ec2-3-232-22-121.compute-1.amazonaws.com",
                                          database="dilabshsjveo3",
                                          user="ogjzilgdyfltod",
                                          password="2a5fff6b7763149071662013def40f9cb2f9f6c8eef3e719f286d8e499ea8471"
                                          )
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
"""
    def __init__(self, username):
        '''
        The connection to the database gets instantiated as part of the constructor
        This makes it so that the connection to the database stays permanent speeds up the process
        '''
        self.username = username

        self.connection = psycopg2.connect(host="ec2-3-232-22-121.compute-1.amazonaws.com",
                                           database="dilabshsjveo3",
                                           user="ogjzilgdyfltod",
                                           password="2a5fff6b7763149071662013def40f9cb2f9f6c8eef3e719f286d8e499ea8471"
                                           )
        self.cursor = connection.cursor()

    def add_transaction(self, transaction):
        ##fee
        postgres_insert_query = "INSERT INTO users Values( %s, %s, %s, %s, %s, %s, %s, %s)"
        record_to_insert = (self.user_name, transaction.coi, longTrade, buyTrade, price, amount, target, time)

        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()

    def getTransaction(self):
        pass
"""
#Database.adduser("admin", "admin@gmail.com", "admin")
#print(Database.checkUsername("admin"))

