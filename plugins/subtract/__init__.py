from commands import Command
from logger import Logger

class SubtractCommand(Command):
    def execute(self, params):
        if len(params) == 2:
            try:
                a, b = map(int, params)  
                result = a - b
                print(result)  
                return result
            except ValueError:
                print("Error: Please provide two valid numbers.")
                Logger.log(f"Invalid input provided for subtraction")
        else:
            print("Error: 'subtract' command requires exactly 2 parameters.")
            Logger.log(f"Subtraction failed")
