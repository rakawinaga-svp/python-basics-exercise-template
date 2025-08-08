import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from compare import compare

def test_equal():
    assert compare(5, 5) == "Equal"

def test_greater():
    assert compare(10, 3) == "Greater"

def test_smaller():
    assert compare(2, 8) == "Smaller"