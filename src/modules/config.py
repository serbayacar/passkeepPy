from configparser import ConfigParser
import os


class Config:
    path = './config.ini'

    def __init__(self):
        config = ConfigParser()
        config.add_section('main')
        config.set('main', 'CONF_TEST', 'TEST_VALUE')
        mode = 'r' if os.path.exists(self.path) is not False else 'w'
        if os.path.exists(self.path) is not True:
            with open(self.path, mode) as f:
                config.write(f)
                f.close()

    def setConfig(self, section, key, value):
        config = ConfigParser()
        config.read(self.path)
        config.set(section, key, value)
        with open('config.ini', 'w') as f:
            config.write(f)
            f.close()
        return

    def getConfig(self, section, key):
        config = ConfigParser()
        config.read(self.path)
        try:
            value = config.get(section, key)
            return value
        except:
            print("Configuration key notfound ({} : {})".format(section, key))
