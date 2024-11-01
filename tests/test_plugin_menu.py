from pathlib import Path
import pytest
from main import MainApp
import os

def test_menu_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch, tmp_path: Path):

    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    with pytest.raises(SystemExit) as e:
        app.load_plugins()
        app.start()
    
 
    assert e.value.code == 0, "The app did not exit as expected"

    out, err = capfd.readouterr()
    
    # Check for the expected plugin names in the output
    assert "The following commands are available:" in out
    assert "add" in out
    assert "subtract" in out
    assert "multiply" in out