import psycopg2
from psycopg2 import Error

class database:

    def connect(self):
        connection = psycopg2.connect(user="postgres",
                                      password="pynative@#29",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")

        cusor = connection.cursor()
        return cursor
    def addUser(self,username, email, password):

        cursor = connect(self)

        cursor.execute("INSERT INTO users VALUES (1, '{username}', '{email}', '{password}')")

        cursor.close()

    def fetchPass(self, username):


    def addTrade(self,username, Trade):
    
    def getCoin(self, coin, username):

    def getAll(self, username):
        '''
        Get all the trades related to a user
        :return:
        '''

