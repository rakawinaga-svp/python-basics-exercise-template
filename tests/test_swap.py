import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from swap import swap

def test_swap_numbers():
    assert swap(5, 10) == (10, 5)

def test_swap_strings():
    assert swap("x", "y") == ("y", "x")

def test_swap_booleans():
    assert swap(True, False) == (False, True)