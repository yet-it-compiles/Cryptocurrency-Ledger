import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

class PasswordEncryption:


    @staticmethod
    def encrypt(password):
        """
        Returns the encrypted password

        :rtype bytes
        :return: hashed value of password
        """
        f = Fernet(os.getenv('KEY')) # could potentially move this elsewhere
        
        encrypted = f.encrypt(self.password.encode())
        return encrypted
    @staticmethod
    def decrypt( encrypted):
        """
        Returns the decrypted password

        :rtype String
        :return: string value of the typed password
        """
        f = Fernet(os.getenv('KEY')) # repeated code from encrypt, necessary to decrypt
        
        decrypted = f.decrypt(encrypted).decode()
        return decrypted

    @staticmethod
    def comparePass (username, password):

        encrypted = encrypt(password)
        stored = database.getPass(username)

        if stored == encrypted:
            return true

        return false


# These lines are used to test and ensure encryption and decryption works properly
#
# encryptedPassword = PasswordEncryption(os.getenv('PASSWORD')).encrypt()
# print(encryptedPassword)
#
# decryptedPassword = PasswordEncryption(os.getenv('PASSWORD')).decrypt(e)
# print(decryptedPassword)