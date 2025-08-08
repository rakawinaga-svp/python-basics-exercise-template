import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from evenodd import is_even

def test_even():
    assert is_even(4) == True

def test_odd():
    assert is_even(5) == False