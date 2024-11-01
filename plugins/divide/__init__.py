from commands import Command
from logger import Logger

class DivideCommand(Command):
    def execute(self, params):
        if len(params) != 2:
            print("Error: 'divide' command requires exactly 2 parameters.")
            return None
        
        try:
            a, b = map(int, params)  # Convert parameters to integers
            if b == 0:
                print("Error: Cannot divide by zero.")
                Logger.log(f"Invalid input for division")
                return None
            result = a / b
            print(result)  # Output the result
            return result
        except ValueError:
            print("Error: Please provide two valid numbers.")
            Logger.log(f"Division failed")
            return None