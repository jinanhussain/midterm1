from commands import Command
from logger import Logger

class SubtractCommand(Command):
    def execute(self, params):
        if len(params) == 2:
            
            a, b = map(int, params)  
            result = a - b
            print(result)  
            return result
        
        else:
            print("Error: 'subtract' command requires exactly 2 parameters.")
            Logger.log(f"Subtraction failed")