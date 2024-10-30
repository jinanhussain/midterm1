from commands import Command

class AddCommand(Command):
    def execute(self, params):
        if len(params) == 2:
            a, b = params
            print(int(a) + int(b))
            