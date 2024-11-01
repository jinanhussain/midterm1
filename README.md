Calculator Midterm Project
This project is a command-based application designed to support arithmetic operations, history management, and logging. The system is built with modularity in mind, allowing commands to be implemented as plugins, which makes the code easily extensible. The application allows for commands like addition, subtraction, multiplication, and division, along with additional functionality such as clearing and reading command history.

project_root/
│
├── .github/workflows/         # GitHub actions for CI/CD (automated testing)
│   └── python-app.yml
├── commands/                  # Command interface and handler
│   └── __init__.py
├── data/                      # Data storage for history
│   └── history.csv
├── plugins/                   # Plugin modules (commands)
│   ├── add/
│   ├── clear_history/
│   ├── divide/
│   ├── greet/
│   ├── menu/
│   ├── multiply/
│   ├── read_history/
│   └── subtract/
├── tests/                     # Unit tests for all components
│   ├── test_app.py
│   ├── test_plugin_add.py
│   ├── test_plugin_clear_history.py
│   ├── test_plugin_divide.py
│   ├── test_plugin_greet.py
│   ├── test_plugin_menu.py
│   ├── test_plugin_multiply.py
│   ├── test_plugin_read_history.py
│   └── test_plugin_subtract.py
├── .gitignore
├── README.md                  # Project documentation
├── logger.py                  # Logger utility for application logging
├── main.py                    # Main application entry point
└── requirements.txt           # List of dependencies


Main Components
Main Application (main.py)

The main application manages user input and command execution:
- MainApp Class: Initializes the command handler, loads plugins, and manages the main program loop.
- load_plugins(): Dynamically loads command plugins from the plugins directory.
- register_plugin_commands(): Registers each command with the command handler.
- appendToHistory(): Logs each command to history.csv.
- start(): Runs the REPL loop, handling user inputs until the user exits.

Commands Module (commands/)
This module contains:

- Command Class (commands/__init__.py): Abstract base class that each plugin inherits, ensuring each command has an execute method.
- CommandHandler Class: Manages command registration and execution.
- register_command(): Registers commands by name.
- execute_command(): Executes commands based on user input, using try-except for error handling (EAFP - Easier to Ask for Forgiveness than Permission).

Plugins Module (plugins/)
Each plugin is a separate command implementing the Command class:

- add (add/__init__.py): Adds two numbers.
- subtract (subtract/__init__.py): Subtracts one number from another.
- multiply (multiply/__init__.py): Multiplies two numbers.
- divide (divide/__init__.py): Divides two numbers, with a check for zero division.
- clear_history (clear_history/__init__.py): Clears all entries in history.csv.
- read_history (read_history/__init__.py): Reads and displays past commands from history.csv.
- menu (menu/__init__.py): Lists available commands.
- greet (greet/__init__.py): Greets the user.

Logger Module (logger.py)
The Logger class provides structured logging with multiple levels (INFO, WARNING, ERROR, CRITICAL). Based on the environment variable LOG_LEVEL, it logs messages accordingly.

- log(): Determines log level and calls the respective log method.
- writeToFile(): Writes log entries to a file specified by LOG_OUTPUT.
- Static Logging Methods: Includes info, warning, error, and critical for structured logs with timestamps.
- History File (data/history.csv)
- Stores command history, where each entry includes the command name and parameters.
- Updated by the MainApp class whenever a command is executed.


Testing
All tests are located in the tests/ directory, with pytest as the testing framework.

test_app.py: Tests the main application flow, including command execution and error handling.
test_plugin_ files*: Each file tests a specific plugin (e.g., test_plugin_add.py tests AddCommand).

To run all tests, use pytest

Example of Test Coverage
- test_plugin_add.py: Ensures AddCommand correctly outputs the result of adding two numbers.
- test_plugin_clear_history.py: Confirms clear_history command empties the history file.
- test_plugin_divide.py: Verifies division logic, handling cases like division by zero.


How to Use
Starting the Application: Run the main script: python main.py
Command Usage:

Enter commands as [command] [param1] [param2].
Type menu to see available commands, exit to quit.

**Example Commands:
- add 5 3: Adds 5 and 3.
- subtract 9 4: Subtracts 4 from 9.
- multiply 7 8: Multiplies 7 by 8.
- divide 12 3: Divides 12 by 3 (returns an error if dividing by zero).

Design Patterns and Key Principles

Design Patterns
This project leverages key design patterns to enhance modularity, maintainability, and extensibility:

Command Pattern: Each command (e.g., AddCommand, SubtractCommand, DivideCommand) is implemented as a separate class that inherits from an abstract Command class. This encapsulates each operation, making it easy to add new commands without modifying the core application. The CommandHandler class acts as a central hub to register and execute these commands, maintaining a clean and extensible design.

Implementation: You can find the Command base class and CommandHandler implementation in commands/__init__.py, and individual commands in their respective files under the plugins directory.
Factory Method: The application dynamically loads command plugins through the load_plugins() method in the MainApp class. This method scans the plugins directory, imports each command module, and registers it with the CommandHandler. This design allows new commands to be added simply by creating a new plugin file in the plugins directory, without modifying the main application code.

Error Handling Principles
Look Before You Leap (LBYL): Some commands, like DivideCommand, check parameters before executing.
Easier to Ask for Forgiveness than Permission (EAFP): CommandHandler attempts to execute commands and handles exceptions if a command doesn’t exist, providing flexibility and robustness.

Environment Variables
Environment variables are used to configure certain aspects of the application without hardcoding them, making the application more flexible and secure. In this project, the .env file contains two variables:

LOG_OUTPUT: Specifies the file path for logging outputs.
LOG_LEVEL: Sets the logging level, allowing control over which messages are logged based on severity (DEBUG, INFO, WARNING, ERROR, CRITICAL).
The application reads these environment variables using the dotenv package in the logger.py module. This setup allows users to modify the logging behavior and output location without altering the code. For example, by setting LOG_LEVEL=DEBUG, the application will log all debug-level messages, while setting it to ERROR would only log error-level messages and higher. You can view this implementation in logger.py.

Logging
The logging system is implemented in the Logger class within logger.py. The class provides various logging methods (info, warning, error, critical), each adding a timestamp and severity level to the log messages. Based on the LOG_LEVEL environment variable, the main log() method decides which logging method to invoke. Each message is printed to the console and written to a file specified by LOG_OUTPUT, ensuring that all relevant information is stored persistently. This logging mechanism is used throughout the application for tracking command execution and error handling, providing useful insights into the application's runtime behavior and simplifying debugging.
c
This documentation provides a full overview of your project's structure, setup, functionality, and testing approach. Each component is designed with modularity in mind, ensuring that your code is organized, extensible, and easy to maintain. Let me know if you need further details on any section!
