from datetime import datetime
class Logger:
    
    @staticmethod
    def writeToFile(message):
          # Open the file in append mode
        with open('logs.txt', 'a') as file:
            # Write or append text to the file
            file.write(message + "\n") 

    @staticmethod
    def debug(message):
        time = datetime.now()
        log = "{} - DEBUG: {}".format(time, message)
        print(log)
        Logger.writeToFile(log)

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

