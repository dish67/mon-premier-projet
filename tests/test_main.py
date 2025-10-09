import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import bonjour, DEFAULT_NAME

def test_bonjour_default():
    msg = bonjour()
    assert DEFAULT_NAME in msg
    assert "Bonjour" in msg

def test_bonjour_custom():
    msg = bonjour("Martine")
    assert "Martine" in msg
    assert "Bonjour" in msg

