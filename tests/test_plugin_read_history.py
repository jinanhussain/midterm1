import pytest
from main import MainApp
import pandas as pd
import os

def setup_history_file(tmp_path, data=None):
    """Helper function to create a mock history file with optional data."""
    file_path = tmp_path / "history.csv"
    if data:
        df = pd.DataFrame(data, columns=["command"])
        df.to_csv(file_path, index=False)
    else:
        # Create an empty DataFrame if no data is provided
        pd.DataFrame(columns=["command"]).to_csv(file_path, index=False)
    return file_path

def test_read_history_command_with_data(capfd, monkeypatch, tmp_path):
    """Test that 'read_history' correctly reads and displays the history file content."""
    
    # Set up a temporary history file with data
    file_path = setup_history_file(tmp_path, data=[{"command": "add 1 2"}, {"command": "multiply 3 4"}])

    # Simulate REPL input for `read_history` followed by `exit`
    inputs = iter(['read_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run the app and configure it to use the temporary history file path
    app = MainApp()
    app.history_file = str(file_path)  # Assuming MainApp can use a custom history file path

    with pytest.raises(SystemExit):
        app.load_plugins()
        app.start()
    
    # Capture the output
    captured = capfd.readouterr()
    assert "add 1 2" in captured.out and "multiply 3 4" in captured.out, "Expected history data not displayed."

def test_read_history_command_with_params(capfd, monkeypatch):
    """Test that 'read_history' command with parameters produces an error."""
    
    # Simulate REPL input for `read_history` with extra parameters, followed by `exit`
    inputs = iter(['read_history extra_param', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run the app
    app = MainApp()
    with pytest.raises(SystemExit):
        app.load_plugins()
        app.start()

    # Capture the output
    captured = capfd.readouterr()
    assert "Error: 'read_history' command does not require parameters." in captured.out, "Expected parameter error message not found."

def test_read_history_command_file_does_not_exist(capfd, monkeypatch, tmp_path):
    """Test that 'read_history' gives an error if the history file does not exist."""
    
    # Set up a path to a non-existent history file
    file_path = tmp_path / "non_existent_history.csv"

    # Simulate REPL input for `read_history` followed by `exit`
    inputs = iter(['read_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run the app and configure it to use the non-existent file path
    app = MainApp()
    app.history_file = str(file_path)  # Assuming MainApp can use a custom history file path

    with pytest.raises(SystemExit):
        app.load_plugins()
        app.start()

    # Capture the output
    captured = capfd.readouterr()
    assert "Error: History file does not exist." in captured.out, "Expected non-existent file error message not found."

def test_read_history_command_empty_file(capfd, monkeypatch, tmp_path):
    """Test that 'read_history' correctly handles an empty history file."""
    
    # Set up an empty history file
    file_path = setup_history_file(tmp_path)

    # Simulate REPL input for `read_history` followed by `exit`
    inputs = iter(['read_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run the app and configure it to use the temporary history file path
    app = MainApp()
    app.history_file = str(file_path)  # Assuming MainApp can use a custom history file path

    with pytest.raises(SystemExit):
        app.load_plugins()
        app.start()

    # Capture the output
    captured = capfd.readouterr()
    assert "History is empty." in captured.out, "Expected empty history message not found."