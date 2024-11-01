from commands import Command
import pandas as pd
import os

class ClearHistoryCommand(Command):
    def execute(self, params):
        if params:
            print("Error: 'clear_history' command does not require parameters.")
            return
        
        file_path = 'data/history.csv'
        if not os.path.exists(file_path):
            print("Error: History file does not exist.")
            return
        
        try:
            # Create an empty DataFrame with the original column headers
            columns = ['command']  # Adjust these to match your actual column names
            empty_df = pd.DataFrame(columns=columns)
            empty_df.to_csv(file_path, index=False)
            print("History cleared successfully.")
        except Exception as e:
            print(f"Error clearing history: {e}")