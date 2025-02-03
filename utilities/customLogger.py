import logging

class LogGen:
    @staticmethod
    def logGen():
        fhandler = logging.FileHandler(".\\Logs\\automation1.log")
        formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s", "%m/%d/%Y %I:%M:%S %p")
        fhandler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger