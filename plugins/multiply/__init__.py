from commands import Command

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
        else:
            print("Error: 'multiply' command requires exactly 2 parameters.")