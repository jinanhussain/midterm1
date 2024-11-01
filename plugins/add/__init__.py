from commands import Command
from logger import Logger

class AddCommand(Command):
    def execute(self, params):
        if len(params) == 2:
            try:
                a, b = map(int, params)  # Convert parameters to integers
                result = a + b
                print(result)  # Output the result
                return result
            except ValueError:
                print("Error: Please provide two valid numbers.")
                Logger.log(f"Invalid input for addition")
        else:
            print("Error: 'add' command requires exactly 2 parameters.")
            Logger.log(f"Addition failed")