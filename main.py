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
from logger import Logger


class MainApp:
    def __init__(self):
        ## make environment variables and stuff
        self.command_handler = CommandHandler()
        return
    def load_plugins(self):
        plugins_package = 'plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            Logger.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e: 
                    Logger.error(f"Error importing plugin {plugin_name}: {e}")
                    return

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                Logger.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")


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


    def start(self):
        while True:
            value = input("Enter an input or enter 'menu' to view options: ")
            value = value.strip().lower()
        
            try:
                self.command_handler.execute_command(value)
            except Exception as e: 
                print(e)
                Logger.error(f"Execute command failed with error {e}")

    
if __name__ == "__main__":
    app = MainApp()
    app.load_plugins()
    app.start()
