from commands import Command

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
        else:
            print("Error: 'subtract' command requires exactly 2 parameters.")