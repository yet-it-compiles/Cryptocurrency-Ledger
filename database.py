import psycopg2
from psycopg2 import Error


class database:

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
                print("PostgreSQL connection is closed")

    def getPass(self):

        cusor.execute(f"SELECT pass FROM users WHERE  username = {username}")
        result = cursor.fetchone()

        if result == "None":
            return error
        else:
            return result

    @staticmethod
    def checkUsername(name):
        pass


database.adduser("hinduhops", "arieshgroevr@gmail", "password")
