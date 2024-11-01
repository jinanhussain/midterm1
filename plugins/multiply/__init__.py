from commands import Command
from logger import Logger

class MultiplyCommand(Command):
    def execute(self, params):
        if len(params) == 2:
                
            a, b = map(int, params)  # Convert parameters to integers
            result = a * b
            print(result)  # Output the result
            return result
        else:
            print("Error: 'multiply' command requires exactly 2 parameters.")
            Logger.log(f"Multiplication failed")
