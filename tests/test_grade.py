import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grade import grade

def test_A():
    assert grade(92) == 'A'

def test_B():
    assert grade(85) == 'B'

def test_C():
    assert grade(75) == 'C'

def test_F():
    assert grade(60) == 'F'