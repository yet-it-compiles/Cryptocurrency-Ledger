import psycopg2
from psycopg2 import Error


class database:
    @staticmethod
    def adduser(name, email, password):
        '''
        Method for adding the user for the first time. Its static so that
        the whole class does not need to be instantiated
        '''

        try:
            connection = psycopg2.connect(host="ec2-3-232-22-121.compute-1.amazonaws.com",
                                          database="dilabshsjveo3",
                                          user="ogjzilgdyfltod",
                                          password="2a5fff6b7763149071662013def40f9cb2f9f6c8eef3e719f286d8e499ea8471"
                                          )

            cursor = connection.cursor()
            postgres_insert_query = "INSERT INTO users Values( %s, %s, %s)"
            record_to_insert = (name, email, password)

            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()

            count = cursor.rowcount
            print(count, "Record inserted successfully into mobile table")

        except(Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()

    @staticmethod
    def get_pass(name):

        try:
            connection = psycopg2.connect(host="ec2-3-232-22-121.compute-1.amazonaws.com",
                                          database="dilabshsjveo3",
                                          user="ogjzilgdyfltod",
                                          password="2a5fff6b7763149071662013def40f9cb2f9f6c8eef3e719f286d8e499ea8471"
                                          )
            cursor = connection.cursor()
            postgres_select_query = "Select password FROM users WHERE  username = %s"

            cursor.execute(postgres_select_query, (name,))

            result = cursor.fetchone()
            if result == None:
                return false
            return true
        except(Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()

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
            if result == None:
                return false
            return true
        except(Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()

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

    def add_transaction(self, coin_name, longTrade, buyTrade, price, amount, target, time):

        postgres_insert_query = "INSERT INTO users Values( %s, %s, %s, %s, %s, %s, %s, %s)"
        record_to_insert = (username, coin_name, longTrade, buyTrade, price, amount, target, time)

        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
    
    def getTransaction(self):
        pass




#database.adduser("hinduhops", "arieshgroevr@gmail", "password")
#database.checkUsername("hindops")