"""Utilities"""
import importlib
import pathlib

import dotenv


def reload_module(module):
    """Reload an imported module"""
    return importlib.reload(module)


def load_dotenv():
    """Load the project .env file"""
    dotenv_path = pathlib.Path(__file__).resolve().parent / ".env"
    dotenv.load_dotenv(dotenv_path=dotenv_path)
