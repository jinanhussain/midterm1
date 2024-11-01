import pytest
from main import MainApp

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command and outputs 'Hello, World!'."""
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    with pytest.raises(SystemExit) as e:
        app.load_plugins()
        app.start()
    
 
    assert e.value.code == 0, "The app did not exit as expected"


    out, err = capfd.readouterr()

    assert "Hello User" in out, "The 'greet' command did not produce the expected output."