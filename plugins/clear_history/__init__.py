from commands import Command
import pandas as pd

class ClearHistoryCommand(Command):
    def execute(self, params):
        print("clearing")
        file_path = 'data/history.csv'
        df = pd.read_csv(file_path)
        df = df.drop(df.index[0:])
        df.to_csv(file_path, index=False)

