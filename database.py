import psycopg2
from psycopg2 import Error

class database:

    def __init__(self, username):
        '''
        The connection to the database gets instantiated as part of the constructor

        This makes it so that the connection to the database stays permanent speeds up the process
        '''
        self.username = username

        self.connection = psycopg2.connect(user="postgres",
                                      password="pynative@#29",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")
        self.cursor = connection.cursor()

    @staticmethod
    def adduser(name, email, password):
        '''
        Method for adding the user for the first time. Its static so that
        the whole class does not need to be instantiated
        '''
        connection = psycopg2.connect(user="postgres",
                                      password="pynative@#29",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")

        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO users (\'{name}\', \'{email}\', \'{password}\'")

        cursor.close()
        connection.close()

    
