import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_dir = r"C:\Users\Darshan Nagaraj\PycharmProjects\Framework1\Logs"
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, "automation.log")

        logging.basicConfig(filename=log_file,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

