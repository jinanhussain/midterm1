from datetime import datetime
import os
from dotenv import load_dotenv

class Logger:
    load_dotenv()
    @staticmethod
    def writeToFile(message):
        log_output = os.getenv('LOG_OUTPUT')
        with open(log_output, 'a') as file:
            # Write or append text to the file
            file.write(message + "\n") 

    @staticmethod
    def debug(message):
        time = datetime.now()
        log = "{} - DEBUG: {}".format(time, message)
        print(log)
        Logger.writeToFile(log)

    @staticmethod
    def log(message):
        log_level = os.getenv('LOG_LEVEL')
        print(log_level)
        if log_level == 'DEBUG':
            Logger.debug(message)
        elif log_level == 'INFO':
            Logger.info(message)
        elif log_level == 'ERROR':
            Logger.error(message)
        elif log_level == 'WARNING':
            Logger.warning(message)
        elif log_level == 'CRITICAL':
            Logger.critical(message)
    

    @staticmethod
    def info(message):
        time = datetime.now()
        log = "{} - INFO: {}".format(time, message)
        print(log)
        Logger.writeToFile(log)
    

    @staticmethod
    def warning(message):
        time = datetime.now()
        log = "{} - WARNING: {}".format(time, message)
        print(log)
        Logger.writeToFile(log)


    @staticmethod
    def error(message):
        time = datetime.now()
        log = "{} - ERROR: {}".format(time, message)
        print(log)
        Logger.writeToFile(log)
  
    @staticmethod
    def critical(message):
        time = datetime.now()
        log = "{} - CRITICAL: {}".format(time, message)
        print(log)
        Logger.writeToFile(log)