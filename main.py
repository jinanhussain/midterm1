from plugins.add import AddCommand
from plugins.subtract import SubtractCommand
from plugins.multiply import MultiplyCommand
from plugins.divide import DivideCommand
import csv
import pandas as pd
import os
import pkgutil
import importlib
from commands import Command
from commands import CommandHandler



class MainApp:
    def __init__(self):
        ## make environment variables and stuff
        self.command_handler = CommandHandler()
        return
    def load_plugins(self):
        plugins_package = 'plugins'
        plugins_path = plugins_package.replace('.', '/')
        print(plugins_path)
        if not os.path.exists(plugins_path):
            print("hello")
           # logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        print(plugins_path)
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            print("hello")
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    print(plugin_module)
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    return 
                 #   logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        print(plugin_name)
        print(plugin_module)
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
               # Command names are now explicitly set to the plugin's folder name
               self.command_handler.register_command(plugin_name, item())
               # logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")




    def appendToHistory(self, cmd, num1, num2):
        file_path = 'data/history.csv'
        existing_data = pd.read_csv(file_path)
        new_data = pd.DataFrame({
            'command': [cmd],
            'num1': [num1],
            'num2': [num2]    
        })
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        updated_data.to_csv(file_path, index=False)
    def clearHistory(self): 
        file_path = 'data/history.csv'
        df = pd.read_csv(file_path)
        df = df.drop(df.index[0:])
        df.to_csv(file_path, index=False)
    def readHistory(self): 
        file_path = 'data/history.csv'
        df = pd.read_csv(file_path)
        print(df) 

    def start(self):
        while True:
            value = input("Enter an input: ")
            value = value.strip().lower()
            if value == "clear":
                self.clearHistory()
                continue 
            if value == "read":
                self.readHistory()
                continue 


           # userInput = value.split() 
           # cmd = userInput[0]
            
            #num1 = userInput[1]
            #num2 = userInput[2]


            # historyCommandList = {"load": LoadCommand, "save" }
            commandList = {"add": AddCommand, "subtract": SubtractCommand, "multiply": MultiplyCommand, "divide": DivideCommand}
            try:
                #commandClass = commandList[cmd]
                #commandClass.execute(self, params=(num1, num2))
                self.command_handler.execute_command(value)
            except Exception as e: 
                print(e)


            ## try to append cmd, num1, num2 to history file

            ## create plugins for Load, save, clear, and delete 
            #self.appendToHistory(cmd, num1, num2)
    

            # AddCommand.execute(self, params=(num1, num2))

    
if __name__ == "__main__":
    app = MainApp()
    app.load_plugins()
    app.start()
