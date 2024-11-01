from commands import Command

class GreetCommand(Command):
    def execute(self, params):
        # logging.info("Hello User")
        print("Hello User")