from src.modules.crypto import Crypto


class Password():
    count = 8
    charset = 'alphanumeric'

    def __init__(self, count, charset):
        # self.count =  6 if count is not None else int(count)
        # self.charset = 'alphanumeric' if charset is not None else str(charset)
        self.count =  int(count) if count is not None else 8
        self.charset =  str(charset) if charset is not None else 'alphanumeric'
        return None

    def generate(self):
        password = Crypto.generate(self.count, self.charset)
        return password

