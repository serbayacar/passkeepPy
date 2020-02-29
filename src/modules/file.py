
class File:
    path = ''

    def __init__(self, path):
        self.path = path

    def write(self, data, permission = 'a'):
        file = open(self.path, permission)
        file.write(data + '\n')
        file.close()
        return

    def reset(self, data, permission = 'w'):
        file = open(self.path, permission)
        file.seek(0)
        file.write(data)
        file.close()
        return

    def read(self, permission = 'r'):
        file = open(self.path, permission)
        file.seek(0)
        lines = file.read()
        file.close()
        return lines