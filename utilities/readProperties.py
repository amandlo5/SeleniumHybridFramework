import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getBaseUrl():
        url = config.get("common info","base_url")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common info","username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info","password")
        return password

    @staticmethod
    def getFilePath():
        file = config.get("common info","file")
        return file