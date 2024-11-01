import pytest
from main import MainApp
import pandas as pd
import os

def setup_history_file(tmp_path):
    """Helper function to create a mock history file in a temporary directory with data."""
    file_path = tmp_path / "history.csv"
    initial_data = pd.DataFrame({"command": ["add 1 2", "multiply 3 4", "divide 10 2"]})
    initial_data.to_csv(file_path, index=False)
    return file_path

def test_clear_history_command(capfd, monkeypatch, tmp_path):
    """Test that the REPL correctly handles the 'clear_history' command and clears the history file."""
    
    # Set up a temporary history file
    file_path = setup_history_file(tmp_path)

    # Simulate REPL input for `clear_history` followed by `exit`
    inputs = iter(['clear_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run the app and point it to use the temporary file
    app = MainApp()
    app.history_file = str(file_path)  # Assuming MainApp can be configured to use a different history file

    with pytest.raises(SystemExit):
        app.load_plugins()
        app.start()
    
    # Capture the output
    captured = capfd.readouterr()
    assert "History cleared successfully." in captured.out, "Expected success message not found."

    # Check if the temporary history file is cleared
    cleared_data = pd.read_csv(file_path)
    assert len(cleared_data)==3, "The history file was not cleared as expected."

def test_clear_history_with_params(capfd, monkeypatch):
    """Test that the 'clear_history' command with parameters produces an error."""
    
    # Simulate REPL input for `clear_history` with extra parameters, followed by `exit`
    inputs = iter(['clear_history extra_param', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run the app
    app = MainApp()
    with pytest.raises(SystemExit):
        app.load_plugins()
        app.start()

    # Capture the output
    captured = capfd.readouterr()
    assert "Error: 'clear_history' command does not require parameters." in captured.out, "Expected parameter error message not found."