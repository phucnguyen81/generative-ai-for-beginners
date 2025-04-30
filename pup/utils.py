"""Utilities"""
import importlib


def reload_module(module):
    """Reload an imported module"""
    return importlib.reload(module)
