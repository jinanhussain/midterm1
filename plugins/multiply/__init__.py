from commands import Command
from logger import Logger

class MultiplyCommand(Command):
    def execute(self, params):
        if len(params) == 2:
            try:
                a, b = map(int, params)  # Convert parameters to integers
                result = a * b
                print(result)  # Output the result
                return result
            except ValueError:
                print("Error: Please provide two valid numbers.")
                Logger.log(f"Invalid input for multiplication")
        else:
            print("Error: 'multiply' command requires exactly 2 parameters.")
            Logger.log(f"Multiplication failed")