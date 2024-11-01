from commands import Command
import pandas as pd
import os

class ClearHistoryCommand(Command):
    def execute(self, params):
        if params:
            print("Error: 'clear_history' command does not require parameters.")
            return
        
        file_path = 'data/history.csv'
        columns = ['command']  # Adjust these to match your actual column names
        empty_df = pd.DataFrame(columns=columns)
        empty_df.to_csv(file_path, index=False)
        print("History cleared successfully.")