import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\Darshan Nagaraj\PycharmProjects\Framework1\Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def readurl():
        url = config.get("LoginCreds", "url")
        return url

    @staticmethod
    def readusername():
        username = config.get("LoginCreds", "username")
        return username

    @staticmethod
    def readpassword():
        password = config.get("LoginCreds", "password")
        return password
