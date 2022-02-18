import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import database
from database import *
load_dotenv()


class PasswordEncryption:

    @staticmethod
    def encrypt(user_password):
        """
        Takes in the user password, and returns an encrypted password

        :param user_password: The users' password
        :type user_password: # TODO
        :rtype: bytes
        :return: hashed value of password
        """
        secret_key = Fernet(os.getenv('KEY'))

        encrypted_password = secret_key.encrypt(self.user_password.encode())
        return encrypted_password

    @staticmethod
    def decrypt(encrypted_password):
        """
        Takes in an encrypted password, and returns a decrypted password

        :param encrypted_password: encrypted password
        :type encrypted_password: bytes
        :return: a decrypted password
        """

        secret_key = Fernet(os.getenv('KEY'))  # repeated code from encrypt, necessary to decrypt

        decrypted_password = secret_key.decrypt(encrypted_password).decode()
        return decrypted_password

    @staticmethod
    def password_comparison(username, password):
        """
        #TODO

        :param username:
        :type username:
        :param password:
        :type password:
        :rtype: bool
        :return:
        """
        #encrypted = PasswordEncryption.encrypt(password)
        stored = Database.get_pass(username)


        print(f"From Database: {stored[0]} and from user {password}")
        db = stored[0]
        if db == password:
            return True

        return False

# These lines are used to test and ensure encryption and decryption works properly
#
# encryptedPassword = PasswordEncryption(os.getenv('PASSWORD')).encrypt()
# print(encryptedPassword)
#
# decryptedPassword = PasswordEncryption(os.getenv('PASSWORD')).decrypt(e)
# print(decryptedPassword)
