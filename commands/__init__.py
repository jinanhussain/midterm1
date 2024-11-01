from abc import ABC, abstractmethod
import pandas as pd

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def appendToHistory(self, full_command):
        file_path = 'data/history.csv'
        existing_data = pd.read_csv(file_path)
        new_data = pd.DataFrame({
            'command': [full_command],   
        })
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        updated_data.to_csv(file_path, index=False)

    def execute_command(self, full_command: str):
       
        try:
            command_name = full_command.split()[0]
            params=[]
            if len(full_command.split()) > 1:
                params = full_command.split()[1:]
            self.commands[command_name].execute(params)
            self.appendToHistory(full_command)
        
        except KeyError:
            print(f"No such command: {command_name}")
