import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

class PasswordEncryption:
    password = ""

    def __init__(self, password):
        """
        Parameterized constructor which initializes the string password
        """
        self.password = password

    def encrypt(self):
        """
        Returns the encrypted password

        :rtype bytes
        :return: hashed value of password
        """
        f = Fernet(os.getenv('KEY')) # could potentially move this elsewhere
        
        encrypted = f.encrypt(self.password.encode())
        return encrypted
    
    def decrypt(self, encrypted):
        """
        Returns the decrypted password

        :rtype String
        :return: string value of the typed password
        """
        f = Fernet(os.getenv('KEY')) # repeated code from encrypt, necessary to decrypt
        
        decrypted = f.decrypt(encrypted).decode()
        return decrypted

# These lines are used to test and ensure encryption and decryption works properly
#
# encryptedPassword = PasswordEncryption(os.getenv('PASSWORD')).encrypt()
# print(encryptedPassword)
#
# decryptedPassword = PasswordEncryption(os.getenv('PASSWORD')).decrypt(e)
# print(decryptedPassword)