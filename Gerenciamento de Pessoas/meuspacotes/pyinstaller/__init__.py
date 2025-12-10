# paths.py
import sys
import os

def get_base_path():
    """
    Return the folder that should be considered the base path for resources.
    Works both when running as a script and when frozen by PyInstaller.
    """
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def resource_path(relative_path):
    """
    Return the absolute path to a resource bundled with the app.
    Example: resource_path('pessoas.txt') -> absolute path to pessoas.txt
    """
    base = get_base_path()
    return os.path.join(base, relative_path)
