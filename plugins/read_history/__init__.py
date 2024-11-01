from commands import Command
import pandas as pd
import os

class ReadHistoryCommand(Command):
    def execute(self, params):
        if params:
            print("Error: 'read_history' command does not require parameters.")
            return
        
        file_path = 'data/history.csv'
        # if not os.path.exists(file_path):
        #     print("Error: History file does not exist.")
        #     return
        df = pd.read_csv(file_path)
        print("Loaded history:", len(df))
        