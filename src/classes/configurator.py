from src.modules.config import Config

class Configurator:
    path = "./config.ini"
    section = 'main'
    configObj = None

    def __init__(self):
        self.configObj = Config( self.path, self.section )
        return

    def setConfig(self, key, value):
        try:
            self.configObj.setConfig(self.section, key, value)
        except:
            raise Warning(f"Configuration key not set successfull!")
        return

    def getConfig(self, key):
        try:
            value = self.configObj.getConfig(self.section, key)
        except:
            raise Warning(f"Configuration key notfound ({self.section} : {key})!")
        
        return value