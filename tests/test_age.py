import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from age import main
import builtins

def test_greet(monkeypatch, capsys):
    inputs = iter(['Alice', '21'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr().out
    assert captured.strip() == "Hello, Alice!\nYou were born in 2004."