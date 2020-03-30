import os
from configparser import ConfigParser


class Config:

    def __init__(self, path, section):
        self.section = section
        self.path = path

        config = ConfigParser()
        config.add_section(self.section)
        config.set(self.section, "CONF_TEST", "TEST_VALUE")
        mode = "r" if os.path.exists(self.path) is not False else "w"
        if os.path.exists(self.path) is not True:
            with open(self.path, mode) as f:
                config.write(f)
                f.close()

    def setConfig(self, section, key, value):
        config = ConfigParser()
        config.read(self.path)
        config.set(section, key, value)
        with open(self.path, "w") as f:
            config.write(f)
            f.close()
        return

    def getConfig(self, section, key):
        config = ConfigParser()
        config.read(self.path)
        value = config.get(section, key)
        return value