from commands import Command
import pandas as pd

class ReadHistoryCommand(Command):
    def execute(self, params):
        print("clearing")
        file_path = 'data/history.csv'
        df = pd.read_csv(file_path)
        print(df) 
