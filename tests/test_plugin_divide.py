import pytest
from main import MainApp

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command and outputs 'Hello, World!'."""
    inputs = iter(['divide 4 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))


    app = MainApp()
    with pytest.raises(SystemExit) as e:
        app.load_plugins()
        app.start()
    
  
    assert e.value.code == 0, "The app did not exit as expected"


    out, err = capfd.readouterr()
    

    assert "2" in out, "The 'divide' command did not produce the expected output."

def test_divide_more_params(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command and outputs 'Hello, World!'."""
    inputs = iter(['divide 4 2 9', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    with pytest.raises(SystemExit) as e:
        app.load_plugins()
        app.start()
    out, err = capfd.readouterr()

    assert "Error: 'divide' command requires exactly 2 parameters." in out, "The 'divide' command did not produce the expected output."
            

def test_divide_0(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command and outputs 'Hello, World!'."""
    inputs = iter(['divide 4 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    with pytest.raises(SystemExit) as e:
        app.load_plugins()
        app.start()
    out, err = capfd.readouterr()

    assert "Error: Cannot divide by zero." in out, "The 'divide' command did not produce the expected output."
            
def test_divide_NAN(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command and outputs 'Hello, World!'."""
    inputs = iter(['divide 4 a', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    with pytest.raises(SystemExit) as e:
        app.load_plugins()
        app.start()
    out, err = capfd.readouterr()

    assert "Error: Please provide two valid numbers." in out, "The 'divide' command did not produce the expected output."
            