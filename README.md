**CALCULATOR MIDTERM PROJECT**

**LINK TO MY VIDEO:** https://drive.google.com/file/d/1oOp6fm0WBeXy2h5err5ht4TY6aE7GNUp/view?usp=sharing



**OVERVIEW**: This project is a command-based application that supports arithmetic operations, history management, and logging. It is built using a modular, extensible architecture, allowing for each command to be implemented as a plugin. This design enables easy addition of new commands without modifying the core application, and it provides robust logging and error-handling mechanisms for maintainability.


**TABLE OF CONTENTS**

1. Setup Instructions
2. Usage Examples
3. Design Patterns
  - Command Pattern
  - Factory Method
4. Environment Variables
5. Logging Strategy
6. Error Handling: LBYL and EAFP
7. File Structure


**SETUP INSTRUCTIONS**
1. clone the repository:
git clone <repository-url>
cd <repository-folder>

2. Install Dependencies:
pip install -r requirements.txt

3. Environment Configuration: Create a .env file in the root directory with the following variables:
LOG_OUTPUT=logs.txt  # Path to log output file
LOG_LEVEL=INFO       # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)



5. Prepare History File: Ensure data/history.csv exists with header:
command


**USAGE EXAMPLES**
1. Starting the Application: Run the main script:
python main.py

2. Entering Commands:
Commands follow the format: [command] [param1] [param2].
Type menu to see a list of available commands, and exit to quit the application.

3. Example Commands:

add 5 3: Adds 5 and 3.
subtract 9 4: Subtracts 4 from 9.
multiply 7 8: Multiplies 7 by 8.
divide 12 3: Divides 12 by 3 (returns an error if dividing by zero).

**DESIGN PATTERNS**

1. Command Pattern

The Command Pattern is central to the application’s extensibility. Each command (such as AddCommand, SubtractCommand, DivideCommand) is implemented as a separate class inheriting from the Command abstract class. This approach encapsulates each operation, making it easy to add new commands without modifying the core application.

Implementation: The Command base class and CommandHandler for managing commands are implemented in commands/__init__.py. Each individual command (e.g., AddCommand, DivideCommand) is implemented in its own file within the plugins directory, following the Command Pattern to isolate command logic.

2. Factory Method
The application uses a Factory Method in load_plugins() within main.py to dynamically load and register plugins (commands) from the plugins directory. This method scans the directory, imports each command module, and registers it with the CommandHandler. By doing so, it allows new commands to be added simply by creating a new plugin file without modifying the existing application code.

Implementation: The Factory Method that dynamically loads and registers commands can be found in main.py, specifically within the load_plugins() function.
These design patterns enable the application to be modular, maintainable, and easily extensible for future functionality.

**ENVIORNMENT VARIABLES**
Environment variables are used to configure certain aspects of the application without hardcoding values, making the application more flexible and secure. In this project, the .env file contains two variables:

LOG_OUTPUT: Specifies the file path for the log output file.
LOG_LEVEL: Sets the logging level, allowing control over which messages are logged based on severity (DEBUG, INFO, WARNING, ERROR, CRITICAL).
The application reads these environment variables in the logger.py module using the dotenv package. This setup enables users to adjust the logging behavior and output location without altering the code itself. For example, setting LOG_LEVEL=DEBUG will log all debug-level messages, while setting it to ERROR will only log error-level messages and above.

Implementation: You can see how environment variables are loaded and utilized in logger.py, specifically in the Logger class.


**LOGGING STRATEGY**

The logging system is implemented through the Logger class in logger.py, which provides structured logging with multiple levels (INFO, WARNING, ERROR, CRITICAL). Depending on the LOG_LEVEL environment variable, the main log() function decides which logging method to invoke, such as info(), warning(), error(), or critical().

Each log entry includes a timestamp and severity level, and is both printed to the console and written to a file specified by LOG_OUTPUT. This central logging strategy keeps the application organized and provides a clear record of important events, including command executions and errors.

By centralizing logging in the Logger class, the application can maintain consistent logs that are easy to review for debugging and monitoring purposes.

Implementation: The detailed logging system, including level-based logging, is implemented in logger.py.


**Error Handling: LBYL and EAFP**

The application uses two common Python error-handling principles:

Look Before You Leap (LBYL):

LBYL is used in commands like DivideCommand to check for potential errors before executing, such as verifying that the divisor is not zero before performing the division.
Implementation: You can find this approach in the execute() method of plugins/divide/__init__.py, where it checks if the divisor is zero to prevent a ZeroDivisionError.
Easier to Ask for Forgiveness than Permission (EAFP):

EAFP is used in the CommandHandler's execute_command() method, where the application attempts to execute a command and handles any KeyError if the command does not exist. This method allows the program to attempt an action and gracefully handle failures as they occur.
Implementation: The EAFP error-handling principle is implemented in commands/__init__.py, specifically in the execute_command() method, where a KeyError is caught if an unregistered command is attempted.
This combination of LBYL and EAFP provides a robust and flexible error-handling strategy, allowing the application to handle predictable errors proactively and unexpected errors reactively.

