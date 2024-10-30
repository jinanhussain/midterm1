from plugins.add import AddCommand
from plugins.subtract import SubtractCommand
from plugins.multiply import MultiplyCommand
from plugins.divide import DivideCommand


class MainApp:
    def __init__(self):
        ## make environment variables and stuff
        return
   
    def start(self):
        while True:
            value = input("Enter an input: ")


            userInput = value.split() # add 1 3 ['add', 1, 3]
            cmd = userInput[0]
            
            num1 = userInput[1]
            num2 = userInput[2]


            # historyCommandList = {"load": LoadCommand, "save" }
            commandList = {"add": AddCommand, "subtract": SubtractCommand, "multiply": MultiplyCommand, "divide": DivideCommand}
            try:
                commandClass = commandList[cmd]
                commandClass.execute(self, params=(num1, num2))
            except:
                print("failed")

            ## try to append cmd, num1, num2 to history file

            ## create plugins for Load, save, clear, and delete 
            appendToHistory(cmd, num1, num2)


            # AddCommand.execute(self, params=(num1, num2))

    
if __name__ == "__main__":
    app = MainApp()
    app.start()