import pytest
from main import MainApp


def test_app_start_exit_command(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = MainApp()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    inputs = iter(['abc', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    
    with pytest.raises(SystemExit) as excinfo:
        app.start()

    captured = capfd.readouterr()
    assert "No such command: abc" in captured.out

def test_add_more_params(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command and outputs 'Hello, World!'."""
    inputs = iter(['add 4 2 9', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    with pytest.raises(SystemExit) as e:
        app.load_plugins()
        app.start()
    out, err = capfd.readouterr()

    assert "Error: 'add' command requires exactly 2 parameters." in out, "The 'add' command did not produce the expected output."
            
