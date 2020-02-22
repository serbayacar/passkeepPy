from cryptography.fernet import Fernet

import random
import string

class Crypto:
    alghoritym = 'SHA256'
    charset = ''
    secretKey = ''
    publicKey = ''

    def __init__(self):
        self.charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

    def encryptData(self, data):
        f = Fernet(self.secretKey)
        encrypted = f.encrypt(message)
        return encrypted

    def decryptData(self, encrypted):
        f = Fernet(self.secretKey)
        decrypted = f.decrypt(encrypted)
        return decrypted

    def generate(self, count, charset = None):
        charDict = {
            'lower': string.ascii_lowercase,
            'upper': string.ascii_uppercase,
            'alpha': string.ascii_uppercase + string.ascii_lowercase,
            'numeric': string.digits,
            'alphanumeric': string.ascii_lowercase + string.ascii_uppercase + string.digits
        }
        if charset is not None:
            self.charset = charDict.get(charset)

        generatedKey = ''.join(random.choice(self.charset) for i in range(count))
        return generatedKey