from commands import Command
import pandas as pd

def readHistory(self): 
        file_path = 'data/history.csv'
        df = pd.read_csv(file_path)
        print(df) 