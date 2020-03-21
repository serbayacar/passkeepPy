import random
import string

from cryptography.fernet import Fernet


class Crypto:
    algorithm = "SHA256"
    secret_key = ""
    public_key = ""

    def __init__(self):
        self.charset = string.ascii_lowercase + string.ascii_uppercase \
        + string.digits

    def encryptData(self, data):
        f = Fernet(self.secret_key)
        encrypted = f.encrypt(message)
        return encrypted

    def decryptData(self, encrypted):
        f = Fernet(self.secret_key)
        decrypted = f.decrypt(encrypted)
        return decrypted

    @staticmethod
    def generate(count, charset=None):
        charDict = {
            "lower": string.ascii_lowercase,
            "upper": string.ascii_uppercase,
            "alpha": string.ascii_uppercase + string.ascii_lowercase,
            "numeric": string.digits,
            "alphanumeric": string.ascii_lowercase
            + string.ascii_uppercase
            + string.digits,
        }
        if charset is not None:
            charset = charDict.get(charset)

        generated_key = "".join(random.choice(charset) for i in range(count))
        print(generated_key);
        # exit(1);
        return generated_key