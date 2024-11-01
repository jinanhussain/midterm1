import pytest
from main import MainApp
import os

def test_menu_command(capfd, monkeypatch, tmp_path):
    """Test that the 'menu' command lists available plugins correctly."""

    # Create a temporary plugins directory with dummy plugin files
    plugins_path = tmp_path / "plugins"
    plugins_path.mkdir()
    
    # Create dummy plugin files in the temporary plugins directory
    (plugins_path / "add.py").touch()
    (plugins_path / "subtract.py").touch()
    (plugins_path / "multiply.py").touch()

    # Simulate REPL input for `menu` command followed by `exit`
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run the app with the temporary plugins directory
    app = MainApp()
    
    # Monkeypatch the plugins path
    monkeypatch.setattr('plugins', str(plugins_path))

    with pytest.raises(SystemExit):
        app.load_plugins()
        app.start()

    # Capture the output
    captured = capfd.readouterr()
    
    # Check for the expected plugin names in the output
    assert "The following commands are available:" in captured.out
    assert "add" in captured.out
    assert "subtract" in captured.out
    assert "multiply" in captured.out