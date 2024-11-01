import pytest
from main import MainApp
import pandas as pd
import os

def setup_history_file(tmp_path):
    """Helper function to create a mock history file in a temporary directory with data."""
    file_path = tmp_path / "history.csv"
    if data is None:
        data = {"command": ["add 1 2", "multiply 3 4", "divide 10 2"]}
    initial_data = pd.DataFrame(data)
    initial_data.to_csv(file_path, index=False)
    return file_path

def test_read_history_command(capfd, monkeypatch, tmp_path):
    """Test that the 'read_history' command with parameters produces an error."""
    
    # Simulate REPL input for `read_history` with extra parameters, followed by `exit`
    inputs = iter(['read_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    file_path = "data/history.csv"
    data = {"command": ["add 1 2", "multiply 3 4", "divide 10 2"]}
    initial_data = pd.DataFrame(data)
    initial_data.to_csv(file_path, index=False)

    # Run the app
    app = MainApp()
    with pytest.raises(SystemExit):
        app.load_plugins()
        app.start()

    # Capture the output
    captured = capfd.readouterr()
    # assert "Error: 'read_history' command does not require parameters." in captured.out, "Expected parameter error message not found."
    assert "Loaded history: 3" in captured.out, "Expected parameter error message not found."

def test_read_history_with_params(capfd, monkeypatch):
    """Test that the 'read_history' command with parameters produces an error."""
    
    # Simulate REPL input for `read_history` with extra parameters, followed by `exit`
    inputs = iter(['read_history extra_param', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    file_path = "data/history.csv"
    data = {"command": ["add 1 2", "multiply 3 4", "divide 10 2"]}
    initial_data = pd.DataFrame(data)
    initial_data.to_csv(file_path, index=False)

    # Run the app
    app = MainApp()
    with pytest.raises(SystemExit):
        app.load_plugins()
        app.start()

    # Capture the output
    captured = capfd.readouterr()
    # assert "Error: 'read_history' command does not require parameters." in captured.out, "Expected parameter error message not found."
    assert "Error: 'read_history' command does not require parameters." in captured.out, "Expected parameter error message not found."


