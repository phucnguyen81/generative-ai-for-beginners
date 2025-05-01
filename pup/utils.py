"""Utilities"""
import importlib
import pathlib
import json

import dotenv


def reload_module(module):
    """Reload an imported module"""
    return importlib.reload(module)


def load_dotenv():
    """Load the project .env file"""
    dotenv_path = pathlib.Path(__file__).resolve().parent / ".env"
    dotenv.load_dotenv(dotenv_path=dotenv_path)


def write_json(data, filepath: pathlib.Path):
    """Write data to file in json format"""
    with filepath.open("w", encoding="utf-8") as file:
        json.dump(data, file)


def read_json(filepath: pathlib.Path):
    """Read json data from file"""
    with filepath.open("r", encoding="utf-8") as file:
        return json.load(file)
